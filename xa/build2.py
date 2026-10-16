import re, markdown, json
src=open('/workspace/daily-article/2026-10-15/x-article.md').read().split('\n')
i=[k for k,l in enumerate(src) if l.startswith('====')][0]
body=src[i+1:]
ops=[]; buf=[]; code=None; hn=0
def flush():
    global buf,hn
    if any(x.strip() for x in buf):
        h=markdown.markdown('\n'.join(buf))
        fn=f'h{hn:03d}.html'; hn+=1
        open(fn,'w').write('<html><head><meta charset="utf-8"></head><body>'+h+'</body></html>')
        ops.append({'t':'html','f':fn})
    buf=[]
for l in body:
    if code is not None:
        if l.startswith('```'): ops.append({'t':'code','lang':code[0],'code':'\n'.join(code[1])}); code=None
        else: code[1].append(l)
        continue
    m=re.match(r'> 📷 \[IMAGE (\d+): .*?\] caption: (.*)',l)
    if m: flush(); ops.append({'t':'img','n':int(m.group(1)),'cap':m.group(2)}); continue
    if l.startswith('```'): flush(); code=[l[3:].strip(),[]]; continue
    buf.append(l)
flush()
json.dump(ops,open('ops.json','w'))
for k,o in enumerate(ops): print(k,o['t'],o.get('f',o.get('n',o.get('lang'))))
