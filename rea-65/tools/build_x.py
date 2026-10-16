import re
from PIL import Image, ImageDraw
R='/workspace/rea-65/'
s=open(R+'article.md').read()
lines=s.split('\n'); title=lines[0].lstrip('# ').strip(); body=lines[1:]
# group image lines by section heading
sec=-1; groups={}; order=[]
for i,l in enumerate(body):
    if l.startswith('## ') or l.startswith('### '): sec=i
    m=re.match(r'!\[(.*?)\]\((img/[^)]+)\)',l)
    if m and 'cover' not in m.group(2):
        groups.setdefault(sec,[]).append((i,m.group(1),m.group(2)))
        if sec not in order: order.append(sec)
def compose(items,out):
    ims=[]
    for _,_,p in items:
        im=Image.open(R+p).convert('RGB')
        if im.width!=1400: im=im.resize((1400,int(im.height*1400/im.width)))
        if p.split('/')[-1].startswith('w') and im.height>700: im=im.crop((0,0,1400,700))
        ims.append(im)
    gap=14; H=sum(i.height for i in ims)+gap*(len(ims)-1)
    c=Image.new('RGB',(1400,H),(255,255,255)); y=0
    for im in ims: c.paste(im,(0,y)); y+=im.height+gap
    c.save(R+out)
first={}; skip=set()
for n,secid in enumerate(order,1):
    items=groups[secid]; out=f'x/x{n:02d}.png'; compose(items,out)
    first[items[0][0]]=(n,out,' / '.join(c for _,c,_ in items)); skip|={i for i,_,_ in items[1:]}
out=[]; in_code=False; tbl=[]
def flush(tbl):
    rows=[[c.strip() for c in r.strip().strip('|').split('|')] for r in tbl]; hdr=rows[0]; res=[]
    for r in rows[2:]:
        res.append(f"**{r[0]}**: {r[1]}" if len(hdr)==2 else f"**{r[0]}**: " + " · ".join(f"{h}: {c}" for h,c in zip(hdr[1:],r[1:])))
        res.append("")
    return res
for i,l in enumerate(body):
    if l.startswith('```'): in_code=not in_code; out.append(l); continue
    if in_code: out.append(l); continue
    if l.startswith('|'): tbl.append(l); continue
    if tbl: out+=flush(tbl); tbl=[]
    if i in skip: continue
    if i in first:
        n,f,cap=first[i]; out.append(f"> 📷 [IMAGE {n:02d}: {f}]: caption: {cap}"); continue
    if re.match(r'!\[.*cover',l): continue
    out.append(re.sub(r'<(https?://[^>]+)>',r'\1',l))
if tbl: out+=flush(tbl)
n=len(order)
teaser=open(R+'teaser.txt').read().strip()
hdr=f"""# X ARTICLE: paste-ready version (not posted)

TITLE (X Article title field):
{title}

COVER IMAGE (5:2, 1500x500): img/00-cover-1500x500.png (a composite made from a real terminal capture in this article)

HOW TO PASTE: paste one section at a time into X's Article editor. Wherever a "📷 [IMAGE NN: file]" line appears, delete it and insert that file from x/ with the caption shown. There are {n} body images (plus the cover). Where a section had several captures, they're stacked into one image so the total stays at 25 or fewer. Markdown tables were converted to bold-label lines because X Articles don't render tables. Code blocks are kept; apply the editor's code-block formatting to them. Every section opens with an image.

TEASER POST (≤280 chars; X counts the link as 23):
{teaser}

{'='*60}
"""
open(R+'x-article.md','w').write(hdr+'\n'.join(out)); print(n)
