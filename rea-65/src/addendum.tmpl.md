# Addendum: Android, firmware and .NET routes, now tested (REA 6.5.0)

*By Richard ([@P7RIM3](https://x.com/P7RIM3)) · October 14, 2026 (ET) · update for "REA, hands-on" (Oct 13, REA 6.4.0), §10.3, §10.5 and §10.7*

> Yesterday these three sections were docs-only because the engines weren't installed. Today I installed them on the same Grok Bot box (Debian 13, x64, Node 24.21.0, JDK 21, Ghidra 12.1.4) and ran each route with **REA 6.5.0** (npm `rea-agents@6.5.0`) on safe targets: an Apache-2.0 sample APK that REA's own tests pin, and a firmware image and .NET assembly I built myself. All output below is real. Nothing was run on Windows or macOS, and nothing was posted anywhere.

## What changed vs the 6.4.0 article

| 6.4.0 article section | Status yesterday | Status now |
|---|---|---|
| §10.3 Android | "I didn't run these. My box has no JADX, no adb and no APK" | ✅ Package, class search, method decompile (JADX headless 0.7.1), Apktool 3.0.3 resource decode, adb client + device list |
| §10.5 Firmware | "I didn't run it, because Binwalk and Unblob aren't installed" | ✅ Binwalk 3.1.0 regions, Unblob 26.6.4 extraction (with sasquatch), extracted ELF → Ghidra |
| §10.7 .NET | "I had no .NET assembly to test on, so this one's docs-only" | ✅ Artifact metadata, members with IL sizes, `ldstr` literals, call edges, P/Invoke boundary |
| `rea doctor` | `host` unsupported, no JADX check passing | `host` PASS, `jadx` PASS (12 PASS / 4 FAIL; see below) |

## 1. Installing the engines

![Real capture: tool versions and pinned hashes](img/40-term-tools.png)

{{T:t30-tool-installs}}

What I installed, and where REA finds it:

| Engine | Version | How | REA variable |
|---|---|---|---|
| JADX headless MCP | 0.7.1 (`-all.jar`, SHA-256 matches REA's pin) | download from the JADX headless MCP release | `REA_JADX_MCP_JAR` |
| Android platform-tools (adb) | 37.0.1 (adb 1.0.41) | Google's platform-tools zip | `REA_ADB_PATH` |
| Apktool | 3.0.3 | jar + wrapper script | `REA_APKTOOL_COMMAND` |
| Binwalk | 3.1.0 | `cargo install binwalk --version 3.1.0 --locked` (no Linux release binary) | `REA_BINWALK_COMMAND` |
| Unblob | 26.6.4 | Python venv, plus `libmagic1 lz4 zstd p7zip-full e2fsprogs` and [sasquatch](https://github.com/onekey-sec/sasquatch/releases) v4.5.1-6 | `REA_UNBLOB_COMMAND` |
| .NET SDK | 8.0.426 | user-local SDK in `~/.local/dotnet` (only to *build* my test assembly; REA's managed route needs no engine) | none |

Test APK: [Appium ApiDemos](https://github.com/appium/android-apidemos) 6.0.18 debug build (Apache-2.0). Its SHA-256 `a9eecf37…f686` matches the fixture REA's tests use.

## 2. Android (replaces §10.3)

![REA's android-analysis doc at 6.5.0](img/w19-doc-android.png)

![Real capture: inspect-android-package + search-android-classes](img/41-term-android.png)

{{T:t31-android}}

![Real capture: inspect-android-method, decode-android-resources, list-adb-devices](img/42-term-android-method.png)

{{T:t32-android-method}}

Notes:
- `signature_verification: "not_performed"`: REA reports the APK's declarations; it doesn't vouch for the signature.
- `list-adb-devices` says `may_have_started_adb_server: true`. It had, so I ran `adb kill-server` afterwards.
- The device-changing tools (`install_adb_package`, `push_adb_file`, `start_adb_app`) were **not** run. There's no device, and they're side-effecting by design.

![REA's apktool-resource-analysis doc at 6.5.0](img/w22-doc-apktool.png)

## 3. Firmware (replaces §10.5)

![REA's firmware-analysis doc at 6.5.0](img/w20-doc-firmware.png)

My image `lab65-fw.bin` (188,416 bytes) is a 512-byte custom `LAB65FW` header, then an xz-compressed squashfs root filesystem (a Rust daemon `bin/hellod`, `etc/device.conf`, `www/index.html`), then a gzip'd tar with `wifi.conf`, padded to 4 KiB.

![Real capture: Binwalk regions → Unblob extraction → extracted files](img/43-term-firmware.png)

{{T:t33-firmware}}

![Real capture: the extracted ELF opened with REA's Ghidra provider](img/44-term-firmware-ghidra.png)

{{T:t34-firmware-ghidra}}

The one remaining gap (`unknown-chunk-handler`, bytes 0–512) is my custom header, which is correct. On the first run, before sasquatch was installed, Unblob reported `missing-extractor-dependency: sasquatch` for `squashfs_v4_le` and left the rootfs packed. REA surfaced that as an explicit gap instead of a silent "done".

## 4. .NET (replaces §10.7)

![REA's managed-code-analysis doc at 6.5.0](img/w21-doc-managed.png)

My assembly `PromoLab.dll` (.NET 8) is a harmless promo-code *format* checker with one P/Invoke:

```csharp
public sealed class PromoCode
{
    private const string Banner = "PromoLab code formatter v1";
    public static bool IsWellFormed(string code) => code.Length == 8 && code.StartsWith("LAB-") && Checksum(code) % 7 == 3;
    internal static int Checksum(string s) { int acc = 0; foreach (char c in s) acc = acc * 31 + c; return Math.Abs(acc); }
    public string Describe() => Banner;
}
public static class Native { [DllImport("libc", EntryPoint = "getpid")] public static extern int GetPid(); }
```

![Real capture: inspect-managed-artifact, inspect-managed-members, inspect-managed-native-boundaries](img/45-term-dotnet.png)

{{T:t35-dotnet}}

REA never loads or runs the assembly. 6.5.0 adds the decoded `ldstr` literals and a declaring type on every call target, and both show up here.

## 5. rea doctor afterwards

![Real capture: unscoped rea doctor and per-route client inspectors](img/46-term-doctor-all.png)

{{T:t36-doctor-all}}

| Check | Result | Why |
|---|---|---|
| node, host | PASS | Node 24.21.0; Debian 13 is now a supported host |
| ghidra (+7 sub-checks) | PASS | Ghidra 12.1.4, JDK 21.0.12.1 |
| jadx | PASS | `REA_JADX_MCP_JAR` → jadx-headless-mcp 0.7.1 |
| hopper | FAIL | Not installed (Hopper is the macOS default) |
| ida-registration | FAIL | No IDA MCP configured |
| skill:identity, registration:cursor | FAIL (config drift) | Doctor suggests `rea setup`; I didn't run it because it edits client configs |

Doctor has no Binwalk, Unblob, Apktool, adb or TShark check. Apktool, adb and TShark have their own `inspect-*-client` commands (shown above). Binwalk and Unblob are verified by running the route (§3).

## Links

- Android: <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/android-analysis.md>
- Apktool resources: <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/apktool-resource-analysis.md>
- Firmware: <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/firmware-analysis.md>
- Managed / .NET: <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/managed-code-analysis.md>
- Testing / recorded scope: <https://github.com/morluto/rea/blob/rea-agents-6.5.0/docs/testing.md>
- sasquatch: <https://github.com/onekey-sec/sasquatch/releases>
- Appium ApiDemos: <https://github.com/appium/android-apidemos>
