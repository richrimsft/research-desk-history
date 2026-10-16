import re
s=open('/workspace/rea-article/article.md').read()
lines=s.split('\n'); title=lines[0].lstrip('# ').strip(); body=lines[1:]
out=[]; n=0; in_code=False; tbl=[]
def flush(tbl):
    rows=[[c.strip() for c in r.strip().strip('|').split('|')] for r in tbl]; hdr=rows[0]; res=[]
    for r in rows[2:]:
        res.append(f"**{r[0]}**: {r[1]}" if len(hdr)==2 else f"**{r[0]}**: " + " · ".join(f"{h}: {c}" for h,c in zip(hdr[1:],r[1:])))
        res.append("")
    return res
for l in body:
    if l.startswith('```'): in_code=not in_code; out.append(l); continue
    if in_code: out.append(l); continue
    if l.startswith('|'): tbl.append(l); continue
    if tbl: out+=flush(tbl); tbl=[]
    m=re.match(r'!\[(.*?)\]\((img/[^)]+)\)',l)
    if m:
        if 'cover' in m.group(2): continue
        n+=1; out.append(f"> 📷 [IMAGE {n:02d}: {m.group(2).split('/')[-1]}]: caption: {m.group(1)}"); continue
    out.append(re.sub(r'<(https?://[^>]+)>',r'\1',l))
if tbl: out+=flush(tbl)
hdr=f"""# X ARTICLE: paste-ready version

TITLE (X Article title field):
{title}

COVER IMAGE (5:2, 1500x500): img/00-cover-1500x500.png (a composite made from a real terminal capture in this article)

HOW TO PASTE: paste one section at a time into X's Article editor. Wherever a "📷 [IMAGE NN: file]" line appears, delete it and insert that file from img/ with the caption shown. There are {n} body images, numbered in order. Markdown tables were converted to bold-label lines because X Articles don't render tables. Code blocks are kept; apply the editor's code-block formatting to them. Each section opens with an image, as requested.

TEASER POST (≤280 chars; X counts the link as 23):
{open('/workspace/rea-article/teaser.txt').read().strip()}

{'='*60}
"""
open('/workspace/rea-article/x-article.md','w').write(hdr+'\n'.join(out)); print(n)
