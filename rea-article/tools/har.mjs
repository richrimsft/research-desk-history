import { createRequire } from "node:module";
const require = createRequire("/home/box/.local/lib/node_modules/rea-agents/package.json");
const { chromium } = require("playwright-core");
const browser = await chromium.launch({ executablePath: "/usr/bin/google-chrome", headless: true });
const ctx = await browser.newContext({ recordHar: { path: "/workspace/re/lab/web/demo.har" } });
const page = await ctx.newPage();
await page.goto("http://127.0.0.1:8765/", { waitUntil: "networkidle" });
await page.click("#export"); await page.waitForTimeout(1500);
await ctx.close(); await browser.close(); console.log("har ok");
