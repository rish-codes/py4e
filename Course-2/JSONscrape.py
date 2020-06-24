from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_445868.json'
data = urlopen(url, context=ctx).read()
info = json.loads(data)
add = 0
lst = info.get('comments')
for item in lst:
    add = add + int(item['count'])

print(add)
