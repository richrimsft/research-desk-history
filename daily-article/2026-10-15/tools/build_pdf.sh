#!/bin/bash
cd /workspace/daily-article/2026-10-15
~/.local/imgvenv/bin/python - <<'P'
import markdown,re
s=open('article.md').read()
html=markdown.markdown(s,extensions=['fenced_code'])
html=re.sub(r'<p><img alt="([^"]*)" src="([^"]+)" /></p>', r'<figure><img src="\2" alt="\1"/><figcaption>\1</figcaption></figure>', html)
cover='<figure><img src="cover-1500x500.png"/><figcaption>Cover image (1500x500)</figcaption></figure>'
css="""@page{size:A4;margin:15mm 14mm}
body{font-family:'DejaVu Sans',sans-serif;font-size:10.3pt;line-height:1.5;color:#1f2328}
h1{font-size:21pt;line-height:1.2} h2{font-size:14.5pt;border-bottom:1px solid #d0d7de;padding-bottom:3px;margin-top:22px;page-break-after:avoid}
figure{margin:8px 0;page-break-inside:avoid;text-align:center} figure img{max-width:100%;max-height:205mm;border:1px solid #d0d7de}
figcaption{font-size:8.3pt;color:#57606a;margin-top:3px}
pre{background:#f6f8fa;border:1px solid #d0d7de;padding:8px;font-size:7.9pt;white-space:pre-wrap;word-break:break-all}
code{font-family:'DejaVu Sans Mono',monospace;font-size:8.6pt;background:#f6f8fa}
blockquote{border-left:4px solid #d0d7de;margin:8px 0;padding:2px 12px;color:#424a53}
a{color:#0969da;word-break:break-all}"""
open('article.html','w').write(f"<!doctype html><html><head><meta charset='utf-8'><title>1,808 Polymarket wallets never lose. Only 7 hold up.</title><style>{css}</style></head><body>{cover}{html}</body></html>")
P
timeout 120 google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --user-data-dir=/tmp/pdf-profile-1015 --print-to-pdf=/workspace/daily-article/2026-10-15/article.pdf file:///workspace/daily-article/2026-10-15/article.html > /tmp/pdf1015.log 2>&1
echo "chrome exit $?"
