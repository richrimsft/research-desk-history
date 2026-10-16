async (page) => { const START=__I__; const ctx=page.context(); const x=ctx.pages().find(p=>p.url().includes('x.com')); let p2=ctx.pages().find(p=>p.url().includes('localhost'));
await p2.goto('http://localhost:8765/x25/ops.json'); const ops=JSON.parse(await p2.locator('body').innerText()); const log=[];
const focusEnd=async()=>{ await x.locator('[data-block=true]').last().click(); await x.keyboard.press('Control+End'); };
await x.bringToFront();
for(let i=START;i<ops.length;i++){ const o=ops[i];
 if(o[0]==='img'){ await focusEnd(); await x.getByRole('button',{name:'Add Media'}).click(); await x.getByRole('menuitem',{name:'Media'}).click(); await x.getByRole('dialog').locator('input[type=file]').setInputFiles(`/workspace/rea-article/img25/${o[1]}.png`); await x.getByText('Processing media...').waitFor({timeout:5000}).catch(()=>{}); await x.getByText('Processing media...').waitFor({state:'detached',timeout:20000}); log.push('img '+o[1]); }
 else if(o[0]==='code'){ await focusEnd(); await x.getByRole('button',{name:'Add Media'}).click(); await x.getByRole('menuitem',{name:'Code'}).click(); const d=x.getByRole('dialog'); await d.getByRole('textbox',{name:'Add code here'}).fill(o[1]); await d.getByRole('button',{name:'Insert'}).click(); await d.waitFor({state:'detached',timeout:5000}); log.push('code '+i); }
 else { await p2.goto('http://localhost:8765/x25/'+o[1]); await p2.bringToFront(); await p2.locator('body').click(); await p2.keyboard.press('Control+a'); await p2.keyboard.press('Control+c'); await x.bringToFront(); await focusEnd(); const last=x.locator('[data-block=true]').last(); log.push('paste '+o[1]+' lastblock='+JSON.stringify((await last.innerText()).slice(0,30))+' cls='+await last.getAttribute('class')); return {next:i+1, log}; }
}
return {next:ops.length, log}; }
