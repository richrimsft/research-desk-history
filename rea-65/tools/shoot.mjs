import { createRequire } from "node:module";
const require = createRequire("/home/box/.local/lib/node_modules/rea-agents/package.json");
const { chromium } = require("playwright-core");
const jobs = JSON.parse(process.argv[2]);
const browser = await chromium.launch({ executablePath: "/usr/bin/google-chrome", headless: true });
const ctx = await browser.newContext({ viewport: { width: 1400, height: 900 }, deviceScaleFactor: 1, colorScheme: "light" });
for (const j of jobs) {
  const page = await ctx.newPage();
  try {
    await page.goto(j.url, { waitUntil: "networkidle", timeout: 45000 }).catch(()=>{});
    await page.waitForTimeout(j.wait ?? 2000);
    if (j.text) {
      const loc = page.getByText(j.text, { exact: false }).first();
      await loc.scrollIntoViewIfNeeded({timeout:8000}).catch(e=>console.error("noscroll",j.out,e.message));
      await page.evaluate(()=>window.scrollBy(0,-90));
      await page.waitForTimeout(800);
    }
    if (j.scrollY) { await page.evaluate(y=>window.scrollTo(0,y), j.scrollY); await page.waitForTimeout(800); }
    await page.screenshot({ path: j.out, fullPage: false });
    console.log("ok", j.out, await page.title());
  } catch (e) { console.error("fail", j.out, e.message); }
  await page.close(); await new Promise(r=>setTimeout(r, 6000));
}
await browser.close();
