#!/usr/bin/env python3
"""Regenerate Kraken + file inventory sections inside index.html (single-file dashboard)."""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WS = ROOT.parent
INDEX = ROOT / "index.html"
SNAP = WS / "markets" / "snapshots.log"
TRADES = WS / "markets" / "trades.log"
RULES = WS / "markets" / "RULES.md"

MARKER_START = "/*HQ_DATA_START*/"
MARKER_END = "/*HQ_DATA_END*/"


def parse_snapshot(line: str) -> dict:
    # 2026-10-13 10:00 ET total=$108.15 BTC=0.00054272($45.14@83165.5) ...
    out: dict = {"raw": line}
    m = re.match(
        r"^(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}) ET total=\$(?P<total>[\d.]+)\s+(?P<body>.*)$",
        line,
    )
    if not m:
        return out
    out["ts"] = m.group("ts") + " ET"
    out["total"] = float(m.group("total"))
    body = m.group("body")
    note = ""
    if " action=" in body:
        pre, _, rest = body.partition(" action=")
        body = pre
        # action=none (note...)
        am = re.match(r"(?P<action>\S+)\s*(?:\((?P<note>.*)\))?$", rest)
        if am:
            out["action"] = am.group("action")
            note = am.group("note") or ""
    out["note"] = note
    holdings = []
    for tok in body.split():
        hm = re.match(
            r"^(?P<asset>[A-Z]+)=(?P<qty>[\d.]+)(?:\(\$(?P<usd>[\d.]+)@(?P<px>[\d.]+)\))?$",
            tok,
        )
        if hm:
            holdings.append(
                {
                    "asset": hm.group("asset"),
                    "qty": float(hm.group("qty")),
                    "usd": float(hm.group("usd")) if hm.group("usd") else None,
                    "price": float(hm.group("px")) if hm.group("px") else None,
                }
            )
        elif tok.startswith("open_orders="):
            out["open_orders"] = int(tok.split("=", 1)[1])
    out["holdings"] = holdings
    return out


def parse_trade(line: str) -> dict:
    # 2026-10-09 11:05:09 XBTUSD buy limit 0.00054272 @ 82915.6 (user-approved) {...}
    m = re.match(
        r"^(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
        r"(?P<pair>\S+)\s+(?P<side>\S+)\s+(?P<otype>\S+)\s+"
        r"(?P<qty>[\d.]+)\s+@\s+(?P<price>[\d.]+)\s+"
        r"\((?P<reason>[^)]*)\)",
        line,
    )
    if not m:
        return {"raw": line}
    d = m.groupdict()
    d["qty"] = float(d["qty"])
    d["price"] = float(d["price"])
    return d


def file_meta(rel: str) -> dict:
    p = WS / rel
    if not p.exists():
        return {"path": rel, "exists": False}
    st = p.stat()
    return {
        "path": rel,
        "exists": True,
        "bytes": st.st_size,
        "mtime": datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M ET"),
    }


def build_data() -> dict:
    snaps = [ln for ln in SNAP.read_text().splitlines() if ln.strip()] if SNAP.exists() else []
    trades = [ln for ln in TRADES.read_text().splitlines() if ln.strip()] if TRADES.exists() else []
    parsed_snaps = [parse_snapshot(s) for s in snaps]
    parsed_trades = [parse_trade(t) for t in trades]
    latest = parsed_snaps[-1] if parsed_snaps else None
    rules_text = RULES.read_text() if RULES.exists() else ""
    stop_line = 60.0
    m = re.search(r"[Ss]top[- ]trading line moves to \$(\d+)", rules_text)
    if m:
        stop_line = float(m.group(1))
    elif re.search(r"[Ss]top rule:.*below \$(\d+)", rules_text):
        stop_line = float(re.search(r"below \$(\d+)", rules_text).group(1))

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M ET"),
        "user": "@P7RIM3",
        "kraken": {
            "latest": latest,
            "history": parsed_snaps[-8:],
            "trades": parsed_trades,
            "rules": {
                "spot_only": ["BTC", "ETH", "SOL"],
                "no_leverage": True,
                "stop_under_usd": stop_line,
                "summary": (
                    "Spot BTC/ETH/SOL only. No leverage, margin, futures, or shorting. "
                    f"Stop trading if total value drops under ${stop_line:.0f}. "
                    "Limit orders; show user the plan before first trade of a session. "
                    "Max 2 new trades/day; max 50% of USD cash in any one pair."
                ),
            },
        },
        "files": {
            "playbook_pdf": file_meta("rea-project/PLAYBOOK.pdf"),
            "playbook_md": file_meta("rea-project/PLAYBOOK.md"),
            "re_article_pdf": file_meta("re-article/article.pdf"),
            "part2_4k": file_meta("x-followup/part2_4k.mp4"),
            "avatar": file_meta("p7rim3-avatar-square.png"),
            "header": file_meta("p7rim3-header.png"),
            "snapshots_log": file_meta("markets/snapshots.log"),
            "trades_log": file_meta("markets/trades.log"),
        },
    }


def inject(data: dict) -> None:
    if not INDEX.exists():
        raise SystemExit(f"missing {INDEX}; create index.html first")
    html = INDEX.read_text()
    blob = (
        MARKER_START
        + "\nwindow.HQ_DATA = "
        + json.dumps(data, indent=2)
        + ";\n"
        + MARKER_END
    )
    if MARKER_START in html and MARKER_END in html:
        html = re.sub(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
            lambda _m: blob,
            html,
            count=1,
            flags=re.S,
        )
    else:
        raise SystemExit("HQ_DATA markers not found in index.html")
    INDEX.write_text(html)
    print(f"Updated {INDEX} at {data['generated_at']}")
    if data["kraken"]["latest"]:
        print(f"  latest total=${data['kraken']['latest'].get('total')} @ {data['kraken']['latest'].get('ts')}")
    print(f"  trades={len(data['kraken']['trades'])}")


if __name__ == "__main__":
    inject(build_data())
