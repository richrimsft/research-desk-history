import re,markdown,html,json
L=open('x-article-25.md').read().split('\n')
start=next(i for i,l in enumerate(L) if l.startswith('*By Richard'))
L=L[start:]
ops=[];buf=[];cap=None;incode=False;code=[];n=0
def conv(lines):
    out=[];prev=''
    for l in lines:
        if re.match(r'^(\d+\. |- )',l) and prev.strip() and not re.match(r'^(\d+\. |- )',prev): out.append('')
        if l.startswith('### '): l='## '+l[4:]
        elif l.startswith('## '): l='# '+l[3:]
        out.append(l);prev=l
    return markdown.markdown('\n'.join(out),extensions=['sane_lists'])
def flush():
    global buf,cap,n
    body=conv(buf)
    if cap: body='<p><em>'+html.escape(cap)+'</em></p>\n'+body
    if body.strip():
        n+=1;fn=f'p{n:02d}.html'
        open('x25/'+fn,'w').write('<!doctype html><meta charset=utf-8><body>'+body+'</body>');ops.append(['paste',fn])
    buf=[];cap=None
for l in L:
    m=re.match(r'> 📷 \[IMAGE (C\d+): .*?\]: caption: (.*)',l)
    if m: flush();ops.append(['img',m.group(1)]);cap=m.group(2);continue
    if l.startswith('⌨️ [CODE BLOCK START'): flush();incode=True;code=[];continue
    if l.startswith('⌨️ [CODE BLOCK END'):
        incode=False
        lang=code[0][3:].strip() if code and code[0].startswith('```') else ''
        body=[c for c in code if not c.startswith('```')]
        ops.append(['code','\n'.join(body),lang]);continue
    if incode: code.append(l);continue
    if l.strip()=='---': continue
    buf.append(l)
flush()
json.dump(ops,open('x25/ops.json','w'),indent=0)
print(len(ops),sum(o[0]=='img' for o in ops),sum(o[0]=='code' for o in ops),set(o[2] for o in ops if o[0]=='code'))
