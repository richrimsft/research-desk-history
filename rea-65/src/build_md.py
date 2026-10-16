import re,sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src).read()
def rep(m):
    t=open(f"/workspace/rea-65/transcripts/{m.group(1)}.txt").read().rstrip()
    return "```text\n"+t+"\n```"
s=re.sub(r"\{\{T:([\w-]+)\}\}",rep,s)
open(dst,"w").write(s)
