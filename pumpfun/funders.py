import json,subprocess,sys,time
RPC='https://api.mainnet-beta.solana.com'
def rpc(m,p):
  for _ in range(3):
    o=subprocess.check_output(['curl','-s','-X','POST',RPC,'-H','Content-Type: application/json','-d',json.dumps({"jsonrpc":"2.0","id":1,"method":m,"params":p})])
    j=json.loads(o or b'{}')
    if 'result' in j: return j['result']
    time.sleep(1.5)
  return None
r=json.load(open(sys.argv[1])); out={}
for h in (r.get('topHolders') or [])[1:13]:
  w=h['owner']; sigs=rpc('getSignaturesForAddress',[w,{"limit":1000}]) or []
  if not sigs: out[w]=None; continue
  old=sigs[-1]; tx=rpc('getTransaction',[old['signature'],{"maxSupportedTransactionVersion":0,"encoding":"jsonParsed"}])
  f=None
  if tx:
    for ins in tx['transaction']['message']['instructions']:
      pi=ins.get('parsed')
      if isinstance(pi,dict) and pi.get('type')=='transfer' and pi['info'].get('destination')==w: f=(pi['info']['source'],pi['info'].get('lamports',0)/1e9)
  out[w]={'pct':round(h['pct'],2),'ntx':len(sigs),'oldest':old.get('blockTime'),'funder':f}
  print(round(h['pct'],2),w[:8],'ntx',len(sigs),'age_h',round((time.time()-(old.get('blockTime') or time.time()))/3600,1),'funder',f,flush=True)
  time.sleep(0.4)
json.dump(out,open(sys.argv[2],'w'))
