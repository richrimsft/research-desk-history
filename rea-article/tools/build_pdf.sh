#!/bin/bash
cd /workspace/rea-article
~/.local/imgvenv/bin/python - <<'P'
import markdown,re
s=open('article.md').read()
html=markdown.markdown(s,extensions=['tables','fenced_code'])
html=re.sub(r'<p><img alt="([^"]*)" src="([^"]+)" /></p>', r'<figure><img src="\2" alt="\1"/><figcaption>\1</figcaption></figure>', html)
css="""@page{size:A4;margin:16mm 14mm}
body{font-family:'DejaVu Sans',sans-serif;font-size:10.5pt;line-height:1.5;color:#1f2328}
h1{font-size:21pt;line-height:1.2} h2{font-size:15pt;border-bottom:1px solid #d0d7de;padding-bottom:3px;margin-top:22px;page-break-after:avoid} h3{font-size:12pt;page-break-after:avoid}
figure{margin:10px 0;page-break-inside:avoid;text-align:center} figure img{max-width:100%;max-height:200mm;border:1px solid #d0d7de}
figcaption{font-size:8.5pt;color:#57606a;margin-top:3px}
pre{background:#f6f8fa;border:1px solid #d0d7de;padding:8px;font-size:8.3pt;white-space:pre-wrap;word-break:break-all;page-break-inside:avoid}
code{font-family:'DejaVu Sans Mono',monospace;font-size:8.8pt;background:#f6f8fa}
table{border-collapse:collapse;width:100%;font-size:8.6pt;margin:8px 0} th,td{border:1px solid #d0d7de;padding:4px 6px;vertical-align:top;word-break:break-word} th{background:#f6f8fa}
blockquote{border-left:4px solid #d0d7de;margin:8px 0;padding:2px 12px;color:#424a53}
a{color:#0969da;word-break:break-all}"""
open('article.html','w').write(f"<!doctype html><html><head><meta charset='utf-8'><title>REA, hands-on</title><style>{css}</style></head><body>{html}</body></html>")
P
timeout 120 google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --user-data-dir=/tmp/pdf-profile --print-to-pdf=/workspace/rea-article/article.pdf file:///workspace/rea-article/article.html > /tmp/pdf.log 2>&1
echo "chrome exit $?"
