import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

#input = '''html'''

commentinfo = ET.fromstring(html)
#lst = stuff.findall('users/user')
lstt = commentinfo.findall('comments/comment')
print('User count:', len(lstt))
count =0
for item in lstt:
    count += int(item.find('count').text)
print(count)