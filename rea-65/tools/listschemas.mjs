import { spawn } from "node:child_process";
const p = spawn("rea", ["mcp"], { stdio: ["pipe", "pipe", "ignore"] });
let buf = ""; const want = process.argv.slice(2);
p.stdout.on("data", d => { buf += d; let i; while ((i = buf.indexOf("\n")) >= 0) { const l = buf.slice(0, i); buf = buf.slice(i + 1); const m = JSON.parse(l); if (m.id === 2) { for (const t of m.result.tools) if (want.includes(t.name)) console.log(t.name, JSON.stringify(t.inputSchema.properties).slice(0, 1800)); p.kill(); process.exit(0); } if (m.id === 1) { p.stdin.write(JSON.stringify({ jsonrpc: "2.0", method: "notifications/initialized" }) + "\n"); p.stdin.write(JSON.stringify({ jsonrpc: "2.0", id: 2, method: "tools/list" }) + "\n"); } } });
p.stdin.write(JSON.stringify({ jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "2025-06-18", capabilities: {}, clientInfo: { name: "x", version: "1" } } }) + "\n");
