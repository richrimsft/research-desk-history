import re, os
from PIL import Image
R='/workspace/daily-article/2026-10-15/'
s=open(R+'article.md').read(); lines=s.split('\n'); title=lines[0].lstrip('# ').strip(); body=lines[1:]
os.makedirs(R+'x',exist_ok=True)
for f in os.listdir(R+'x'): os.remove(R+'x/'+f)
out=[]; n=0; in_code=False; sec_has_img={}; cur=None
for l in body:
    if l.startswith('```'): in_code=not in_code; out.append(l); continue
    if in_code: out.append(l); continue
    if l.startswith('## '): cur=l; sec_has_img[cur]=False
    m=re.match(r'!\[(.*?)\]\((img/[^)]+)\)',l)
    if m:
        n+=1; im=Image.open(R+m.group(2)).convert('RGB')
        if im.width>1400: im=im.resize((1400,int(im.height*1400/im.width)))
        f=f'x/x{n:02d}.png'; im.save(R+f,optimize=True)
        out.append(f"> 📷 [IMAGE {n:02d}: {f}] caption: {m.group(1)}"); sec_has_img[cur]=True; continue
    out.append(l)
assert all(sec_has_img.values()), [k for k,v in sec_has_img.items() if not v]
teaser=open(R+'teaser.txt').read().strip()
hdr=f"""# X ARTICLE: paste-ready version (REVIEW ONLY, NOT POSTED)

TITLE (X Article title field, {len(title)} characters):
{title}

COVER IMAGE (1500x500): cover-1500x500.png (built from the real funnel numbers in this article)

HOW TO PASTE: paste one section at a time into X's Article editor. Wherever a "📷 [IMAGE NN: file]" line appears, delete that line and insert the file from x/ with the caption shown. There are {n} body images (plus the cover), numbered in order. Every section opens with an image. There are no tables. Code blocks are kept; apply the editor's code-block formatting to them.

TEASER POST ({len(teaser)} characters without a link; a link adds 23):
{teaser}

{'='*60}
"""
open(R+'x-article.md','w').write(hdr+'\n'.join(out)); print('images',n,'title',len(title))
