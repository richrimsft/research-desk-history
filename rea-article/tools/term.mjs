import { createRequire } from "node:module";
import fs from "node:fs";
const require = createRequire("/home/box/.local/lib/node_modules/rea-agents/package.json");
const { chromium } = require("playwright-core");
const jobs = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const esc = s => s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
const browser = await chromium.launch({ executablePath: "/usr/bin/google-chrome", headless: true });
const page = await browser.newPage({ viewport: { width: 1400, height: 400 }, deviceScaleFactor: 1 });
for (const j of jobs) {
  let txt = fs.readFileSync(j.src, "utf8").replace(/\s+$/,"");
  if (j.maxLines) { const l = txt.split("\n"); if (l.length > j.maxLines) txt = l.slice(0, j.maxLines).join("\n") + "\n… (" + (l.length - j.maxLines) + " more lines in the saved transcript)"; }
  const body = esc(txt).replace(/^(\$ .*)$/gm, '<span class="cmd">$1</span>');
  const html = `<!doctype html><html><head><style>
  body{margin:0;background:#0b0f14;font-family:'DejaVu Sans Mono',monospace}
  .win{margin:0;border:1px solid #30363d;background:#0d1117}
  .bar{background:#161b22;color:#8b949e;font:13px 'DejaVu Sans',sans-serif;padding:8px 12px;display:flex;gap:8px;align-items:center}
  .dot{width:12px;height:12px;border-radius:50%;display:inline-block}
  pre{margin:0;padding:14px 18px;color:#c9d1d9;font-size:15px;line-height:1.38;white-space:pre-wrap;word-break:break-all}
  .cmd{color:#7ee787;font-weight:bold}
  .foot{color:#6e7681;font:12px 'DejaVu Sans',sans-serif;padding:6px 12px;border-top:1px solid #21262d}
  </style></head><body><div class="win" id="w"><div class="bar"><span class="dot" style="background:#ff5f56"></span><span class="dot" style="background:#ffbd2e"></span><span class="dot" style="background:#27c93f"></span>&nbsp;${esc(j.title)}</div><pre>${body}</pre><div class="foot">Real output captured on the Grok Bot box (Debian 13, x64) · REA 6.4.0 · ${esc(j.when || "Oct 13, 2026 ET")}</div></div></body></html>`;
  await page.setContent(html);
  await page.locator("#w").screenshot({ path: j.out });
  console.log("ok", j.out);
}
await browser.close();
