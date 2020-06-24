import urllib
import json
import ssl

# Ignore SSL certificate errors
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

params = dict()
api_key = 42
address = 'Smolensk State University'
params['key'] = api_key
params['address'] = address
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

url = serviceurl + urllib.parse.urlencode(params)
print(url)
data = urlopen(url, context=ctx).read().decode()

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('Failure to retrieve data.')

print(json.dumps(js, indent=4))

place_id = js["results"][0]["place_id"]
print(place_id)
