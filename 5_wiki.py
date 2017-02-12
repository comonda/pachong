#!/usr/bin/env python

'this is a py to climb the wiki main page'

import re
from bs4 import BeautifulSoup as bs
from  urllib.request import urlopen

url = 'https://en.wikipedia.org/wiki/Main_Page'

#get html
handler = urlopen(url)
html = handler.read().decode()
handler.close()

#tidy html
soup = bs(html, 'html.parser')

#get the link
list_url  = soup.find_all('a', href=re.compile("^/wiki/"))

#list url
for url in list_url:
    if not re.search(r'\.jpg|JPG$', url['href']):

        print(url.string,' <----> ', 'https://en.wikipedia.org'+url['href'] )