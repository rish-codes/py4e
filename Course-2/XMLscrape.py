from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_445867.xml'
xml = urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)
lst = tree.findall('comments/comment')
add = 0
for item in lst:
    count = int(item.find('count').text)
    add = add + count
print(add)
