import { createRequire } from "node:module";
const require = createRequire("/home/box/.local/lib/node_modules/rea-agents/package.json");
const { chromium } = require("playwright-core");
const [,, html, out, w, h] = process.argv;
const browser = await chromium.launch({ executablePath: "/usr/bin/google-chrome", headless: true });
const page = await browser.newPage({ viewport: { width: +w, height: +h } });
await page.goto("file://" + html); await page.waitForTimeout(500);
await page.screenshot({ path: out, fullPage: !!process.env.FULL }); await browser.close(); console.log("ok", out);
