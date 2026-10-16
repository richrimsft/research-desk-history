# What's new in REA 6.5: SQLite, pcap, WASM, Go, Rust, Electron fuses, Android, firmware and .NET, tested hands-on (with receipts)

*By Richard ([@P7RIM3](https://x.com/P7RIM3)) · October 14, 2026 (ET) · follow-up to yesterday's [REA 6.4.0 hands-on](https://x.com/P7RIM3)*

![Cover: What's new in REA 6.5. Composite of a real REA terminal capture from this article.](img/00-cover-1500x500.png)

> **About the receipts.** REA **6.5.0** ([release page](https://github.com/morluto/rea/releases/tag/rea-agents-6.5.0)) was published **Wed Oct 14, 2026, 8:32 AM ET**. Everything below ran on my Grok Bot box (Debian 13, x64, Node 24.21.0, Ghidra 12.1.4, JDK 21) between about 12:30 and 3:30 PM ET, against the npm package **rea-agents 6.5.0** and a clone of [morluto/rea](https://github.com/morluto/rea) at `75104040d` (`rea-agents-6.5.0-25-g75104040d`). Every terminal image is real output, and the same text is in a code block under it so you can copy it. Every target is something I built myself, or (for Android) an Apache-2.0 sample app that REA's own tests pin. **Nothing here was tested on Windows or macOS.** Where I only read the docs, I say so.

---

## 1. TL;DR: all five gaps from yesterday are closed

![Real capture: the commands missing from 6.4.0 are in 6.5.0's rea --help, and the bundled skill is now version 42](img/13-term-gaps-closed.png)

Yesterday's article flagged that npm 6.4.0 lacked routes the `main` branch already documented: **packet capture (fields), pcap summaries, Go, WASM and SQLite**. The skill on `main` was version 41 while npm shipped 37. Today both are **version 42**, and every one of those routes runs:

| Gap in 6.4.0 | 6.5.0 command / MCP tool | Tested today? | Section |
|---|---|---|---|
| Packet capture (fields) | `inspect-packet-capture` / `inspect_packet_capture` | ✅ TShark 4.4.19 | §8 |
| pcap summaries (DNS / SNI / endpoints) | `inspect-pcap-capture` / `inspect_pcap_capture` | ✅ | §8 |
| Go build metadata | `inspect-go-binary` / `inspect_go_binary` | ✅ go1.24.4 | §10 |
| WASM | `inspect-wasm-artifact`, `compare-wasm-interfaces` | ✅ WABT 1.0.42 | §9 |
| SQLite | `inspect-sqlite-database` / `inspect_sqlite_database` | ✅ SQLite 3.53.4 | §7 |

The release also adds Rust dependency metadata and Electron fuses (both tested, §11–12), plus cross-bundle JavaScript and paged summaries (§4–6). I also installed JADX, adb, Apktool, Binwalk, Unblob and the .NET SDK and ran the three routes I couldn't test yesterday: **Android, firmware and .NET** (§13).

{{T:t04-gaps}}

## 2. Step 1: update, and where that t.co link goes

![The REA 6.5.0 release page on GitHub](img/w01-release.png)

Someone sent me `https://t.co/8VhocJiXYK` with "make sure we are up to date". It's a plain 301 to the 6.5.0 release page, the same tool and version, so there was nothing else to install:

![Real capture: t.co resolves to the 6.5.0 release, published 8:32 AM ET](img/10-term-tco.png)

{{T:t01-tco}}

Then the update itself. npm 11.19 asks before running install scripts, so you'll see a `frida` warning. That only matters if you use REA's optional Frida tools ([docs](https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/frida-instrumentation.md)):

![Real capture: npm install rea-agents@latest, rea --version 6.5.0, git pull](img/11-term-update.png)

{{T:t02-update}}

`main` was already 25 commits past the tag by mid-afternoon. Everything in this article uses the **npm 6.5.0** build, not `main`.

![Real capture: rea doctor --provider ghidra, all nine checks healthy](img/12-term-doctor-ghidra.png)

{{T:t03-doctor-ghidra}}

## 3. The lab: safe local targets I built

![REA's testing guide at 6.5.0: recorded verification scope per route](img/w17-doc-testing.png)

REA is for software you own or are authorized to analyze ([DISCLAIMER](https://github.com/morluto/rea/blob/rea-agents-6.5.0/DISCLAIMER.md)). So I built every target myself in `/workspace/re/lab65`:

| Target | What it is |
|---|---|
| `js/dist/` | 4-file esbuild app: `index.js` → shared chunk, plus two dynamic-import chunks (checkout, settings) |
| `js/wp-dist/` | The same source built with webpack 5.111.1 into 5 files (runtime + split chunks) |
| `sqlite/notes.db` | Read-only 20 KB database: 2 tables, 2 indexes, a view and a trigger, with a max-int64 and a BLOB |
| `pcap/lab65.pcap` | 14 packets made with scapy using RFC 5737 documentation addresses only: DNS, HTTP, a TLS ClientHello with SNI, one UDP datagram |
| `wasm/calc-v1.wasm`, `calc-v2.wasm` | Hand-written WAT, assembled with WABT; v2 adds an import and an export |
| `go/hellogo` | `go build -trimpath` of a hello world that uses `rsc.io/quote` |
| `rust/hellorust-*` | The same crate (dep: `itoa`) built with and without `cargo auditable` |
| `electron/stock`, `electron/hardened` | Electron 44.7.2 Linux binary, once stock, once with fuses flipped by `@electron/fuses` 2.1.3 |
| `android/ApiDemos-debug.apk` | Appium ApiDemos 6.0.18 (Apache-2.0), the exact APK REA's own tests pin (SHA-256 matches) |
| `firmware/lab65-fw.bin` | My own 188 KB image: 512-byte custom header + xz squashfs rootfs + gzip'd config |
| `dotnet/target/PromoLab.dll` | A tiny .NET 8 class library + console app I wrote (one P/Invoke) |

The WASM sources, so you can see exactly what REA should find:

```wat
(module $calc
  (import "env" "log_i32" (func $log (param i32)))
  (memory (export "memory") 1)
  (func $add (export "add") (param i32 i32) (result i32)
    local.get 0 local.get 1 i32.add)
  (func (export "checksum") (param $ptr i32) (param $len i32) (result i32) ...)
)
;; calc-v2.wat adds:
;;   (import "env" "now_ms" (func $now (result f64)))
;;   (func (export "mul") (param i32 i32) (result i32) local.get 0 local.get 1 i32.mul)
```

Env vars for the bring-your-own engines (all documented per route):

```bash
export REA_WABT_BIN_DIRECTORY=$HOME/.local/wabt/wabt-1.0.42/bin
export REA_WAKARU_COMMAND=$HOME/.local/wakaru/wakaru
export REA_TSHARK_COMMAND=/usr/bin/tshark          # must be absolute for inspect-packet-capture
export REA_JADX_MCP_JAR=$HOME/.local/android/jadx-headless-mcp-0.7.1-all.jar
export REA_ADB_PATH=$HOME/.local/android/platform-tools/adb
export REA_APKTOOL_COMMAND=$HOME/.local/apktool/apktool
export REA_BINWALK_COMMAND=$HOME/.cargo/bin/binwalk
export REA_UNBLOB_COMMAND=$HOME/.local/unblob-venv/bin/unblob
```

## 4. JavaScript: analyze only the files you pick

![REA's javascript-recovery doc at 6.5.0](img/w04-doc-js-recovery.png)

**New in 6.5:** `--source-path` (MCP: `source_paths`) analyzes exactly the files you name *without* pulling their imports into scope. Unselected files keep their identity and get explicit *unknown* coverage, not silence ([changelog](https://github.com/morluto/rea/blob/rea-agents-6.5.0/CHANGELOG.md)).

I picked `index.js` and the checkout chunk out of four files:

![Real capture: selected-file analysis. 2 of 4 parsed; the other two inventoried as unknown/unavailable; cross-chunk edges resolved](img/20-term-js-selected.png)

{{T:t06-js-selected}}

What to notice:

- **Only 2 files parsed** (`parsed_javascript_files: 2`). The shared chunk and settings chunk show up twice: once as an observed *asset* (it exists, with its hash), once as `unknown … state=unavailable` with the limitation *"Source is outside the caller-selected source_paths; it was inventoried but not analyzed."*
- **Edges into unselected files still resolve.** Both the static import of the shared chunk and the *named bindings* (`apiBase`, `formatPrice`) are recorded, at `inferred/high`.

Run it again without `--source-path` and coverage goes from `partial` to `complete`:

![Real capture: selected (2 parsed, partial) vs full (4 parsed, complete)](img/21-term-js-full.png)

{{T:t07-js-full}}

## 5. Code-split recovery across webpack chunks

![Wakaru v1.14.0 release, the unbundler REA drives for recovery](img/w18-wakaru.png)

`recover-javascript-sources` now takes **multiple inputs** (`--additional-path`) and keeps cross-chunk imports, using caller-supplied [Wakaru 1.14.0](https://github.com/pionxzh/wakaru/releases/tag/v1.14.0). With one chunk, you get webpack's mangled import. With all five, Wakaru links it to the recovered `src/shared.js`:

![Real capture: one chunk vs all five chunks; the shared import becomes a named import](img/22-term-recover.png)

{{T:t08-recover}}

Receipt: `runtime_equivalence: "unknown"`. REA doesn't claim the recovered code behaves the same, and the original names (`API_BASE`, `formatPrice`) are **not** recovered. You get `$` and `a` back, because that's what the minified bundle contains.

## 6. Compact summaries, then pages (MCP and CLI)

![REA's MCP contract doc: summary delivery and retained-evidence views](img/w11-doc-mcp-summary.png)

This is the change agents will feel most. Pass `detail: "summary"`, get a small result, then page the retained Evidence with `inspect_analysis_view` **without re-running the analysis** ([mcp-contracts.md](https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/mcp-contracts.md)). I drove the MCP server directly over stdio with a 28-line JSON-RPC client:

```json
{"name":"inspect_wasm_artifact","arguments":{"path":".../calc-v1.wasm","detail":"summary"}}
{"name":"inspect_analysis_view","arguments":{
   "source":{"kind":"retained-evidence","evidence_id":"$R4.evidence_id"},
   "view":{"kind":"wasm","facet":"exports","offset":0,"limit":2}}}
```

![Real capture: one MCP session. Summaries for JS, WASM and pcap, then pages with next_offset until exhausted](img/23-term-mcp-paged.png)

{{T:t09-mcp-paged}}

The paging contract is simple and honest: `examined`, `total`, `next_offset`, `exhausted`. WASM exports came back 2 of 3 (`next_offset: 2`), then 1 of 3 (`exhausted: true`).

The CLI has no retained store between processes, so you pass the saved Evidence **inline**. On my 4-file app, the full Evidence was 266,827 bytes and the summary view 9,827 bytes, about 27× smaller (the [CLI guide](https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/cli.md)'s example is a 334 MB Obsidian Evidence file → ~10 KB):

![Real capture: inspect-analysis-view from the CLI, inline Evidence](img/24-term-cli-view.png)

{{T:t10-cli-view}}

## 7. SQLite, offline and read-only

![REA's sqlite-databases doc at 6.5.0](img/w06-doc-sqlite.png)

`inspect-sqlite-database` reads a local snapshot (and an existing sibling WAL) **without modifying it**. It needs **Node 24 ≥ 24.15 or Node 26+** (it uses `DatabaseSync.limits`; see §15 for what Node 20 does). My database file is mode `-r--r--r--`, and REA was fine with that:

![Real capture: inventory. Provider SQLite 3.53.4, file hash, tables, indexes, view, trigger](img/30-term-sqlite.png)

{{T:t11-sqlite}}

Rows are opt-in, per table and column, and typed carefully. Text keeps its raw bytes, the int64 max comes back as a **string** (no JavaScript precision loss), BLOBs are hex, and `order: "unspecified"` tells you not to read meaning into row order:

![Real capture: typed rows, row limit and truncation, and a view rejected as a row source](img/31-term-sqlite-rows.png)

{{T:t12-sqlite-rows}}

Asking for rows from the *view* `pinned_notes` is refused: rows come from **ordinary tables only**.

## 8. Packet captures: summary first, then exact fields

![6.5.0 release notes: Packet captures, recorded on Linux with Wireshark 4.6.6](img/w02-release-packets.png)

Two tools. `inspect-pcap-capture` gives the overview (endpoints, DNS, TLS SNI, HTTP URIs, protocol stacks). `inspect-packet-capture` gives exact TShark fields with a display filter and paging ([pcap-analysis.md](https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/pcap-analysis.md)). Both read a saved file. Neither captures live traffic.

![Real capture: inspect-pcap-capture on my 14-packet lab capture](img/32-term-pcap.png)

{{T:t13-pcap}}

Everything matches what I put in: two DNS answers, SNI `api.example.org`, the HTTP request URI and six protocol stacks. Confidence is `derived` (TShark's dissection, not raw bytes).

![REA's pcap-analysis doc: "Inspect only the needed facts"](img/w05-doc-pcap.png)

Now the exact fields, page 3 of the TCP packets (`--match_offset 6 --match_limit 3`), and the raw payload of my UDP "ping":

![Real capture: inspect-packet-capture fields, paging window and payload bytes](img/33-term-packets.png)

{{T:t14-packets}}

`01026c616236352d70696e67` is `\x01\x02lab65-ping`, exactly what I sent. Recorded upstream coverage is Wireshark 4.6.6; I used Debian's **4.4.19**, and it worked.

## 9. WebAssembly: inspect and compare, never execute

![REA's wasm-artifacts doc at 6.5.0](img/w07-doc-wasm.png)

`inspect-wasm-artifact` uses your own [WABT 1.0.42](https://github.com/WebAssembly/wabt/releases/tag/1.0.42) to validate and list imports and exports, and it can scan loader "glue" JS for references to the module. It **never runs the module** and never fetches anything:

![Real capture: inspect-wasm-artifact. Valid, not executed, 1 import, 3 exports, glue reference found](img/34-term-wasm.png)

{{T:t15-wasm}}

It found the `fetch("calc-v1.wasm")` literal in my glue file at line 4, column 68, and labeled it a `local-path-candidate` (a static literal, not proof of what loads at runtime).

![WABT 1.0.42 release page](img/w14-wabt.png)

`compare-wasm-interfaces` diffs two inspection Evidence records (no WABT needed at compare time). It caught exactly my two additions:

![Real capture: compare v1 → v2. mul and now_ms added, 4 unchanged](img/35-term-wasm-compare.png)

{{T:t16-wasm-compare}}

Snag: the input wants the raw Evidence objects as `left`/`right`. The `{kind:"inline", evidence}` wrapper that `inspect-analysis-view` uses is rejected (§15).

## 10. Go build metadata

![REA's go-binaries doc at 6.5.0](img/w08-doc-go.png)

`inspect-go-binary` reads the embedded buildinfo from ELF, PE or thin Mach-O, without running the file ([go-binaries.md](https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/go-binaries.md)):

![Real capture: inspect-go-binary. go1.24.4, main module, dependency versions, build settings](img/36-term-go.png)

{{T:t17-go}}

That's the exact compiler, module graph and build flags (`-trimpath=true`, `CGO_ENABLED=0`), all `observed`. This is the fastest supply-chain question you can ask of a Go binary.

## 11. Rust dependency lists (cargo-auditable)

![cargo-auditable on GitHub: embeds the dependency tree in a .dep-v0 section](img/w16-cargo-auditable.png)

`inspect-rust-binary` reads the `.dep-v0` section that [cargo-auditable](https://github.com/rust-secure-code/cargo-auditable) embeds ([rust-binaries.md](https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/rust-binaries.md)). I built the same crate twice:

![Real capture: auditable build lists hellorust → itoa 1.0.18; plain build returns null with an honest limitation](img/37-term-rust.png)

{{T:t18-rust}}

The plain build gets the right answer, which is "don't know": *"Absence of .dep-v0 does not mean the binary has no dependencies."* (I used cargo-auditable **0.6.6**. 0.7.7 needs rustc ≥ 1.86.)

![REA's rust-binaries doc at 6.5.0](img/w09-doc-rust.png)

## 12. Electron fuses: stock vs hardened

![Electron's fuses documentation](img/w15-electron-fuses.png)

[Electron fuses](https://www.electronjs.org/docs/latest/tutorial/fuses) are build-time switches like `RunAsNode` and `EnableNodeCliInspectArguments`. `inspect-electron-fuses` reads the fuse wire bytes **without launching the app**, then states what each one implies at runtime ([electron-fuses.md](https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/electron-fuses.md)). I took Electron 44.7.2 and made a hardened copy with `@electron/fuses`:

![Real capture: stock fuses honor --inspect and RunAsNode; hardened fuses do not](img/38-term-fuses.png)

{{T:t19-fuses}}

The stock binary honors `ELECTRON_RUN_AS_NODE` and `--inspect`. The hardened one doesn't, and it only loads `app.asar`. ASAR integrity validation stays **unknown** on Linux even when the fuse is on, because REA won't claim what the platform doesn't enforce. As the changelog puts it, fuse observations *"do not prove other Inspector-enablement paths."*

![REA's electron-fuses doc at 6.5.0](img/w10-doc-fuses.png)

## 13. Android, firmware and .NET (the routes I skipped yesterday)

![REA's android-analysis doc at 6.5.0](img/w19-doc-android.png)

Yesterday I left §10.3 (Android), §10.5 (firmware) and §10.7 (.NET) as docs-only. Today I installed the engines and ran them. Everything is also saved as a standalone addendum (`addendum-android-firmware-dotnet.md`).

![Real capture: pinned JADX jar and APK hashes match REA's fixtures; adb, Apktool, Binwalk, Unblob, sasquatch, .NET SDK versions](img/40-term-tools.png)

{{T:t30-tool-installs}}

### 13.1 Android (JADX headless + Apktool + adb)

![Real capture: inspect-android-package and search-android-classes via jadx-headless-mcp 0.7.1](img/41-term-android.png)

{{T:t31-android}}

![Real capture: one method decompiled to Java, Apktool resource decode, adb device list](img/42-term-android-method.png)

{{T:t32-android-method}}

`signature_verification: "not_performed"` is stated, not hidden. `list-adb-devices` honestly reports `may_have_started_adb_server: true`. It did, so I ran `adb kill-server` afterwards. I didn't touch the device-changing tools (install, push, start) because there's no device.

![REA's apktool-resource-analysis doc at 6.5.0](img/w22-doc-apktool.png)

### 13.2 Firmware (Binwalk 3.1.0 + Unblob 26.6.4 → Ghidra)

![REA's firmware-analysis doc at 6.5.0](img/w20-doc-firmware.png)

![Real capture: Binwalk regions, Unblob extraction, extracted rootfs files](img/43-term-firmware.png)

{{T:t33-firmware}}

Coverage is `partial`, and the **only** gap is my own 512-byte custom header, which no handler knows. That's correct. The first time, the gap was `missing-extractor-dependency: sasquatch` and the squashfs stayed packed (§15). Then the extracted daemon goes straight into the native flow:

![Real capture: the extracted ELF opened with Ghidra; string found at 0x14c000](img/44-term-firmware-ghidra.png)

{{T:t34-firmware-ghidra}}

### 13.3 .NET (static metadata and CIL, no engine)

![REA's managed-code-analysis doc at 6.5.0](img/w21-doc-managed.png)

My assembly is a harmless promo-code *format* checker with one P/Invoke:

```csharp
public static bool IsWellFormed(string code) => code.Length == 8 && code.StartsWith("LAB-") && Checksum(code) % 7 == 3;
[DllImport("libc", EntryPoint = "getpid")] public static extern int GetPid();
```

![Real capture: inspect-managed-artifact, inspect-managed-members (new ldstr literals and declaring types), native boundaries](img/45-term-dotnet.png)

{{T:t35-dotnet}}

New in 6.5 and visible here: decoded **`ldstr` literals** (`"LAB-"`, the banner) and a **declaring type on every call target**. The P/Invoke boundary `GetPid → libc!getpid` is found without loading the assembly.

## 14. rea doctor, the agent connector, and what passes

![REA's client-configuration doc: how Grok Bot connectors are detected](img/w12-doc-grokbot.png)

After installing everything, here's the unscoped doctor:

![Real capture: unscoped rea doctor plus the per-route client inspectors](img/46-term-doctor-all.png)

{{T:t36-doctor-all}}

- **PASS (12):** node, host, ghidra and its 7 sub-checks, **jadx**. `host` passes on Debian 13 today; yesterday's 6.4.0 doctor called it unsupported.
- **FAIL (4):** `hopper` and `ida-registration` (engines I don't have; Hopper is macOS), `skill:identity` and `registration:cursor` (config drift: doctor suggests `rea setup`, which I didn't run because it edits client configs).
- Doctor doesn't check Binwalk, Unblob, WABT or TShark. Use each route's `inspect-*-client` command, or just run the route.

My Grok Bot `rea` connector restarted onto 6.5.0. The proof is that the connector and the CLI produce **the same content-addressed Evidence ID** for the same file:

![Real capture: Grok Bot's rea connector on 6.5.0, same Evidence ID as the CLI](img/39-term-connector.png)

{{T:t20-connector}}

## 15. Troubleshooting: real snags from today

![Real capture: four real errors and what fixes them](img/50-term-snags.png)

{{T:t22-snags}}

| Symptom | Fix |
|---|---|
| `capability_unavailable: Supply absolute REA_TSHARK_COMMAND` | `export REA_TSHARK_COMMAND=/usr/bin/tshark`. `inspect-pcap-capture` finds tshark on PATH; `inspect-packet-capture` insists on an absolute path |
| SQLite → vague `execution_failure` | You're on Node 20 (or Node 22 / early 24). Use Node 24 ≥ 24.15 or 26+ |
| `compare-wasm-interfaces` → `missing_argument left.evidence_id` | Pass the raw Evidence JSON as `left`/`right`, not `{kind:"inline",evidence}` |
| Unblob gap `missing-extractor-dependency: sasquatch` | Install [onekey-sec/sasquatch](https://github.com/onekey-sec/sasquatch/releases) (I used v4.5.1-6). Also `libmagic1`, `lz4`, `zstd`, `p7zip-full`, `e2fsprogs` |
| `apt` can't find `tshark` | `sudo apt-get update` first |
| Binwalk 3.1.0 has no Linux release binary | `cargo install binwalk --version 3.1.0 --locked` |
| `cargo install cargo-auditable` fails on older Rust | `cargo install cargo-auditable --version 0.6.6` (0.7.7 needs rustc 1.86) |
| Agent connector still advertises 6.4.0 tools | Restart or reconnect it, or pin it to `npx -y rea-agents@6.5.0 mcp` |
| npm warns about `frida` install scripts | Harmless unless you use the Frida tools; allow them explicitly if you do |

## 16. Hype vs receipts (short version)

![Real capture: GitHub API star count at 3:03 PM ET](img/51-term-stars.png)

{{T:t21-stars}}

| Claim going around today | Receipt |
|---|---|
| "Pick the JS files you want… trace how pieces connect across bundles" ([@_ttejas_](https://x.com/_ttejas_/status/2110363026419503576)) | **Confirmed.** §4–5: 2 of 4 files parsed, cross-chunk edges and bindings resolved, unselected files marked unknown |
| "893 commits, 529 merged PRs" ([@DavidCabezaAI](https://x.com/DavidCabezaAI/status/2110380913779523836)) | **Matches the release notes' own** [contribution record](https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/releases/6.5.0.contributions.json). For scale: `git rev-list` between the two tags in my clone counts 266 commits on the tag line |
| "334 MB Obsidian analysis → ~10 KB summary" ([@Alexcyzhou](https://x.com/Alexcyzhou/status/2110378930448511031)) | **That's the docs' example**, not something I reproduced. My own receipt: 266,827 → 9,827 bytes on a small app (§6) |
| "6.5 is noticeably faster" ([@qwerty__cs](https://x.com/qwerty__cs/status/2110396867918057724)) | **Not measured.** I didn't benchmark 6.4 vs 6.5 |
| "REA + Opus 5.5 finds exactly why any app is slow, down to the line" ([@0xMitto](https://x.com/0xMitto/status/2110343371122200787)) | **Not a documented REA route.** REA reads code and recorded evidence; it isn't a profiler. Treat line-level "why it's slow" claims as the model's inference |
| Stars | GitHub API: **236,820** at 3:03 PM ET, Oct 14 (yesterday's capture: 204,859 at 6:28 PM ET) |

## 17. What I did *not* test (documented only)

![6.5.0 release notes highlights](img/w03-release-rust-fuses.png)

These are in 6.5.0's release notes, but I didn't run them, so take them as documented, not verified: **sigrok** signal-recording decode (Linux, sigrok-cli 0.7.2), **QUIC qlog** (aioquic 1.5.0), **Fiddler SAZ**, **HarmonyOS** HAP/HSP, **Flutter** APK AOT, **Frida** instrumentation, attached native **IDA** MCP, new **Ghidra** profiles (MIPS, RISC-V, PowerPC, PSP, raw 6502), Ghidra **byte search**, AArch64 recorded crashes, HAR API-surface derivation, and the ADB device-changing tools. Nothing here was run on **Windows** or **macOS**. Two recorded-coverage notes: upstream tested pcap with Wireshark 4.6.6 (I used 4.4.19), and WASM's real-tool lane is macOS arm64 (I ran it on Linux x64).

## 18. Links

![rea.tools, the project site](img/w13-rea-tools.png)

| What | Link |
|---|---|
| 6.5.0 release | <https://github.com/morluto/rea/releases/tag/rea-agents-6.5.0> |
| Changelog at 6.5.0 | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/CHANGELOG.md> |
| npm package | <https://www.npmjs.com/package/rea-agents> |
| Project site | <https://rea.tools/> |
| JS recovery | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/javascript-recovery.md> |
| MCP contracts (summary / views) | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/mcp-contracts.md> |
| CLI guide | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/cli.md> |
| SQLite | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/sqlite-databases.md> |
| Packet captures | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/pcap-analysis.md> |
| WASM | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/wasm-artifacts.md> |
| Go | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/go-binaries.md> |
| Rust | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/rust-binaries.md> |
| Electron fuses | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/electron-fuses.md> |
| Android | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/android-analysis.md> |
| Apktool resources | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/apktool-resource-analysis.md> |
| Firmware | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/firmware-analysis.md> |
| .NET / managed | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/managed-code-analysis.md> |
| Client setup (incl. Grok Bot) | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/client-configuration.md> |
| Testing / recorded scope | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/testing.md> |
| Disclaimer | <https://github.com/morluto/rea/blob/rea-agents-6.5.0/DISCLAIMER.md> |
| WABT 1.0.42 | <https://github.com/WebAssembly/wabt/releases/tag/1.0.42> |
| Wakaru 1.14.0 | <https://github.com/pionxzh/wakaru/releases/tag/v1.14.0> |
| cargo-auditable | <https://github.com/rust-secure-code/cargo-auditable> |
| Electron fuses | <https://www.electronjs.org/docs/latest/tutorial/fuses> |
| sasquatch | <https://github.com/onekey-sec/sasquatch/releases> |
| Appium ApiDemos (Apache-2.0) | <https://github.com/appium/android-apidemos> |

*Analyze only what you own or are authorized to analyze. Every target above is my own build or an Apache-2.0 sample.*
