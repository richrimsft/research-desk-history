import json,subprocess,time,glob,re
T="0816"
def get(u):
  try: return json.loads(subprocess.check_output(['curl','-s','--max-time','20',u]) or b'null')
  except Exception: return None
mints=set()
for l in open('lists.txt'):
  for x in json.loads(l):
    if x.get('chainId')=='solana': mints.add(x['tokenAddress'])
for c in json.load(open(f'pf-live-{T}.json')): mints.add(c['mint'])
for c in json.load(open(f'cands-{T}.json')): mints.add(c['baseToken']['address'])
# priors / watch
prior=set()
for f in glob.glob('autopsy-summary-*.json')+glob.glob('_prior-rejects-*.json')+glob.glob('inwindow-*.json')+glob.glob('new-*.json')+glob.glob('watch-extra-*.json')+glob.glob('rc-*.json'):
  try: s=open(f).read()
  except: continue
  for m in re.findall(r'[1-9A-HJ-NP-Za-km-z]{32,44}',s):
    if m.endswith('pump') or m.endswith('Deer'): prior.add(m)
# pump.fun sorted lists
pfl=[]
for sort in ['market_cap','last_trade_timestamp','created_timestamp']:
  r=get(f'https://frontend-api-v3.pump.fun/coins?offset=0&limit=50&sort={sort}&order=DESC&includeNsfw=false') or []
  if isinstance(r,dict): r=r.get('coins') or []
  if not isinstance(r,list): r=[]
  pfl+=r
  for c in r: mints.add(c['mint'])
json.dump(pfl,open(f'pf-sorted-{T}.json','w'))
qs=['pump','pumpswap','pumpfun','sol','meme','cat','dog','ai','bouncer','crow','irene','deer','roadster','elon','goat','trump','pepe','frog','monkey','based','chase','tesla','grok','x','penguin','bonk','dev','cto','orangutan','robot']
for q in qs:
  r=get(f'https://api.dexscreener.com/latest/dex/search?q={q}')
  if not isinstance(r,dict): r={}
  for p in r.get('pairs') or []:
    if p['chainId']=='solana' and p['dexId'] in ('pumpfun','pumpswap'): mints.add(p['baseToken']['address'])
mints|=set(m for m in prior)
mints=list(mints); pairs=[]; best={}
for i in range(0,len(mints),30):
  r=get('https://api.dexscreener.com/tokens/v1/solana/'+','.join(mints[i:i+30]))
  if not isinstance(r,list): r=[]
  for p in r:
    pairs.append(p); a=p['baseToken']['address']
    if a not in best or (p.get('liquidity') or {}).get('usd',0)>(best[a].get('liquidity') or {}).get('usd',0): best[a]=p
print(len(mints),'mints',len(pairs),'pairs')
json.dump(mints,open(f'expanded-mints-{T}.json','w')); json.dump(list(best.values()),open(f'expanded-{T}.json','w'))
priorfail=set()
for f in glob.glob('autopsy-summary-*.json')+glob.glob('_prior-rejects-*.json')+glob.glob('inwindow-*.json')+glob.glob('rc-*.json'):
  s=open(f).read()
  for m in re.findall(r'[1-9A-HJ-NP-Za-km-z]{32,44}',s): priorfail.add(m)
now=time.time()*1000; iw=[]; young=[]
for a,p in best.items():
  age=(now-(p.get('pairCreatedAt') or now))/3.6e6; mc=p.get('marketCap') or p.get('fdv') or 0
  pc=p.get('priceChange') or {}; t=(p.get('txns') or {}).get('h1') or {}
  row=dict(symbol=p['baseToken']['symbol'],name=p['baseToken']['name'],mint=a,mc=mc,age_h=round(age,2),h1=pc.get('h1'),m5=pc.get('m5'),h24=pc.get('h24'),buys=t.get('buys'),sells=t.get('sells'),vol_h1=(p.get('volume') or {}).get('h1'),dex=p['dexId'],liq=(p.get('liquidity') or {}).get('usd'),url=p.get('url'),pairCreatedAt=p.get('pairCreatedAt'))
  if p['dexId'] not in ('pumpfun','pumpswap') or mc<10000 or not (pc.get('h1') or 0)>0: continue
  if 0.5<=age<=4: row['tag']='PRIOR' if a in priorfail else 'NEW'; iw.append(row)
  elif age<0.5: young.append(row)
iw.sort(key=lambda r:-r['mc']); young.sort(key=lambda r:r['age_h'])
json.dump(iw,open(f'inwindow-{T}.json','w'),indent=1); json.dump({'too_young':young},open(f'watch-extra-{T}.json','w'),indent=1)
json.dump([r for r in iw if r['tag']=='NEW'],open(f'new-{T}.json','w'),indent=1)
for r in iw: print(r['tag'],r['symbol'],round(r['mc']),r['age_h'],r['h1'],r['m5'],r['dex'],r['buys'],r['sells'],r['vol_h1'],r['mint'])
print('--young')
for r in young: print(r['symbol'],round(r['mc']),r['age_h'],r['h1'],r['m5'],r['dex'],r['mint'])
