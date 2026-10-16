import os, time, hmac, hashlib, base64, urllib.parse, urllib.request, json, sys
BASE = "https://api.kraken.com"
def private(path, data=None):
    data = dict(data or {})
    data["nonce"] = str(int(time.time() * 1000))
    post = urllib.parse.urlencode(data)
    msg = (data["nonce"] + post).encode()
    digest = hashlib.sha256(msg).digest()
    mac = hmac.new(base64.b64decode(os.environ["KRAKEN_API_SECRET"]), path.encode() + digest, hashlib.sha512)
    req = urllib.request.Request(BASE + path, post.encode(), {
        "API-Key": os.environ["KRAKEN_API_KEY"],
        "API-Sign": base64.b64encode(mac.digest()).decode(),
        "User-Agent": "signal-markets-desk"})
    return json.load(urllib.request.urlopen(req, timeout=20))
def public(path, params=None):
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    return json.load(urllib.request.urlopen(url, timeout=20))
if __name__ == "__main__":
    print(json.dumps(private("/0/private/Balance")))
