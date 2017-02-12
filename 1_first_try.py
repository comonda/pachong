#!/user/bin/env python

''' the first try to climb
to get the photo from tieba.baidu.com.
'''

import urllib.request
import re


#set url
url = 'http://tieba.baidu.com/p/4969996513'

#get the page
def get_html(url):
    handler = urllib.request.urlopen(url)
    html = handler.read().decode()
    handler.close()
    return html

#analyse and math what you want,then get it out
def get_info(html):
    reg = r'src="(.+?\.jpg)" size'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    return imglist

#save result
def save_result(imglist):
    x = 1
    for img in imglist:
        urllib.request.urlretrieve(img, '/Users/mac/Desktop/pacong/%s.jpg' % x )
        x +=1

#test
html = get_html(url)
imglist = get_info(html)
save_result(imglist)
print('done')



