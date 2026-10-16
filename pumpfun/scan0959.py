import json,subprocess,time
def get(u): return json.loads(subprocess.check_output(['curl','-s',u]) or b'null')
mints=set()
for l in open('lists.txt'):
  l=l.strip()
  if not l: continue
  for x in json.loads(l):
    if x.get('chainId')=='solana' and x['tokenAddress'].endswith('pump'): mints.add(x['tokenAddress'])
for q in ['pump','pumpswap','pumpfun','sol','meme','cat','dog','ai']:
  r=get(f'https://api.dexscreener.com/latest/dex/search?q={q}') or {}
  for p in r.get('pairs') or []:
    if p['chainId']=='solana' and p['baseToken']['address'].endswith('pump'): mints.add(p['baseToken']['address'])
for c in get('https://frontend-api-v3.pump.fun/coins/currently-live?limit=50&offset=0&includeNsfw=false') or []: mints.add(c['mint'])
mints=list(mints); rows=[]
print(len(mints),'mints')
for i in range(0,len(mints),30):
  r=get('https://api.dexscreener.com/tokens/v1/solana/'+','.join(mints[i:i+30])) or []
  best={}
  for p in r:
    a=p['baseToken']['address']
    if a not in best or (p.get('liquidity') or {}).get('usd',0)>(best[a].get('liquidity') or {}).get('usd',0): best[a]=p
  rows+=best.values()
out=[]
for p in rows:
  v=p['volume'].get('h24',0); age=(time.time()*1000-p.get('pairCreatedAt',0))/60000
  if v<20000 or age<30: continue
  pc=p.get('priceChange',{}); t=p.get('txns',{})
  out.append(p)
  print(p['baseToken']['address'],p['baseToken']['symbol'],p['dexId'],'mc',p.get('marketCap'),'liq',(p.get('liquidity')or{}).get('usd'),'v24',round(v),'v1',p['volume'].get('h1'),'ch',pc.get('m5'),pc.get('h1'),pc.get('h24'),'tx1h',t.get('h1'),'age_h',round(age/60,1))
json.dump(out,open('cands-0959.json','w'))
