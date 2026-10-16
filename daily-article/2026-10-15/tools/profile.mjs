import { createRequire } from "node:module";
const require = createRequire("/home/box/.local/lib/node_modules/rea-agents/package.json");
const { chromium } = require("playwright-core");
const browser = await chromium.launch({ executablePath: "/usr/bin/google-chrome", headless: true });
const ctx = await browser.newContext({ viewport: { width: 1400, height: 900 }, colorScheme: "light" });
const page = await ctx.newPage();
await page.goto(process.argv[2], { waitUntil: "networkidle", timeout: 45000 }).catch(()=>{});
await page.waitForTimeout(4000);
await page.getByRole("button", { name: "Continue in view only mode" }).last().click({timeout:8000}).catch(e=>console.error("no modal", e.message));
await page.waitForTimeout(1500);
if (process.argv[4]) { await page.getByText(process.argv[4], {exact:true}).first().click({timeout:5000}).catch(e=>console.error("noclick",e.message)); await page.waitForTimeout(2500); }
await page.screenshot({ path: process.argv[3] });
console.log("ok", await page.title());
await browser.close();
