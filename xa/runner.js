async (page) => { const FROM=__A, TO=__B;
const t0=await page.context().newPage(); await t0.goto('http://localhost:8765/ops.json'); const ops=JSON.parse(await t0.locator('body').innerText()); await t0.close(); await page.bringToFront();
const top=page.locator('[contenteditable=true]').first().locator('[data-contents=true]').first().locator(':scope > *');
async function toEnd(enter){ await top.last().click(); await page.keyboard.press('Control+End'); if(enter) await page.keyboard.press('Enter'); }
const log=[];
for (let k=FROM;k<=TO&&k<ops.length;k++) { const o=ops[k];
 if(o.t==='html'){ const t=await page.context().newPage(); await t.goto('http://localhost:8765/'+o.f); await t.bringToFront(); await t.locator('body').click({position:{x:5,y:5}}); await t.keyboard.press('Control+a'); await t.keyboard.press('Control+c'); await t.waitForTimeout(300); await t.close(); await page.bringToFront(); await toEnd(false); await page.keyboard.press('Control+v'); await page.waitForTimeout(1500); }
 if(o.t==='code'){ await toEnd(true); await page.getByRole('button',{name:'Add Media'}).click(); await page.getByRole('menuitem',{name:'Code'}).click(); const d=page.getByRole('dialog'); await d.getByRole('textbox',{name:'Add code here'}).waitFor();
   const lang={bash:'Bash',python:'Python',json:'JSON'}[o.lang]; if(lang){ await d.getByRole('textbox',{name:'Search programming language'}).fill(o.lang); await d.getByRole('button',{name:lang,exact:true}).click(); }
   await d.getByRole('textbox',{name:'Add code here'}).fill(o.code); await d.getByRole('button',{name:'Insert',exact:true}).click(); await d.waitFor({state:'detached'}); await page.waitForTimeout(800); }
 if(o.t==='img'){ await toEnd(true); await page.getByRole('button',{name:'Add Media'}).click(); await page.getByRole('menuitem',{name:'Media'}).click();
   await page.getByRole('dialog').locator('input[type=file]').setInputFiles(`/workspace/daily-article/2026-10-15/x/x${String(o.n).padStart(2,'0')}.png`);
   await page.getByRole('dialog').waitFor({state:'detached',timeout:15000}); await page.waitForTimeout(1500);
   await page.getByText('Provide a caption (optional)',{exact:true}).last().click(); const d=page.getByRole('dialog'); await d.getByRole('textbox').fill(o.cap); await d.getByRole('button',{name:'Save'}).click(); await d.waitFor({state:'detached'}); }
 log.push(k+o.t);
}
const n=await top.count(); const r=[]; for(let i=Math.max(0,n-3);i<n;i++){ const x=top.nth(i); r.push(i+' '+(await x.innerHTML()).slice(0,20)+' | '+(await x.innerText()).slice(0,80)); } return [log,r]; }
