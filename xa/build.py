import re, markdown, html
src=open('/workspace/daily-article/2026-10-15/x-article.md').read().split('\n')
i=[k for k,l in enumerate(src) if l.startswith('====')][0]
body=src[i+1:]
chunks=[[]]; caps=[]
for l in body:
    m=re.match(r'> 📷 \[IMAGE (\d+): .*?\] caption: (.*)',l)
    if m: caps.append(m.group(2)); chunks.append([])
    else: chunks[-1].append(l)
for n,c in enumerate(chunks):
    h=markdown.markdown('\n'.join(c),extensions=['fenced_code'])
    open(f'c{n:02d}.html','w').write('<html><head><meta charset="utf-8"></head><body>'+h+'</body></html>')
for n,c in enumerate(caps): open(f'cap{n+1:02d}.txt','w').write(c)
print(len(chunks),len(caps))
