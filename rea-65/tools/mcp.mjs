// Minimal MCP stdio client: spawns `rea mcp`, runs a list of calls, prints each result as JSON lines.
// Calls can reference earlier results with "$R<n>.<jq-like path>" strings.
import { spawn } from "node:child_process";
import fs from "node:fs";
const steps = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const out = process.argv[3];
const p = spawn("rea", ["mcp"], { stdio: ["pipe", "pipe", "pipe"], env: process.env });
let buf = "", id = 0; const pending = new Map();
p.stdout.on("data", d => { buf += d; let i; while ((i = buf.indexOf("\n")) >= 0) { const line = buf.slice(0, i); buf = buf.slice(i + 1); if (!line.trim()) continue; const m = JSON.parse(line); if (m.id != null && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); } } });
p.stderr.on("data", () => {});
const rpc = (method, params) => new Promise(r => { const i = ++id; pending.set(i, r); p.stdin.write(JSON.stringify({ jsonrpc: "2.0", id: i, method, params }) + "\n"); });
const get = (o, path) => path.split(".").reduce((a, k) => a?.[k], o);
const results = [];
const resolve = v => typeof v === "string" && /^\$R\d+\./.test(v) ? get(results[+v.match(/^\$R(\d+)/)[1]], v.replace(/^\$R\d+\./, "")) : Array.isArray(v) ? v.map(resolve) : v && typeof v === "object" ? Object.fromEntries(Object.entries(v).map(([k, x]) => [k, resolve(x)])) : v;
const init = await rpc("initialize", { protocolVersion: "2025-06-18", capabilities: {}, clientInfo: { name: "lab65-client", version: "1.0" } });
p.stdin.write(JSON.stringify({ jsonrpc: "2.0", method: "notifications/initialized" }) + "\n");
const log = [];
log.push({ step: "initialize", serverInfo: init.result?.serverInfo });
for (const s of steps) {
  if (s.list) { const r = await rpc("tools/list", {}); const names = r.result.tools.map(t => t.name); results.push({ names }); log.push({ step: "tools/list", count: names.length, match: names.filter(n => new RegExp(s.list).test(n)) }); continue; }
  const args = resolve(s.arguments);
  const r = await rpc("tools/call", { name: s.name, arguments: args });
  const sc = r.result?.structuredContent ?? (r.result?.content?.[0]?.text ? (() => { try { return JSON.parse(r.result.content[0].text); } catch { return r.result.content[0].text; } })() : r.error);
  results.push(sc);
  log.push({ step: s.name, arguments: args, isError: r.result?.isError ?? !!r.error, result: sc });
}
fs.writeFileSync(out, JSON.stringify(log, null, 1));
p.kill(); process.exit(0);
