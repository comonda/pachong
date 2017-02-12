#!usr/bin/env python

'''clibm_with_header.py
climb with header
'''

from urllib import request
import re


url = 'http://www.baidu.com'

#get the page

req = request.Request(url)
req.add_header('User-Agent',"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0")
handler = request.urlopen(req)
html = handler.read()
handler.close()
print(html)
with open('/Users/mac/Desktop/pacong/html', 'wb') as f :
    f.write(html)
print('done')
