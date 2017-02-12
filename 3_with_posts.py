'with posts'

from urllib import parse
from urllib.request import urlopen, Request


#init information
url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
postDate = parse.urlencode([('StartStation', '2f940836-cedc-41ef-8e28-c2336ac8fe68'),
                            ('EndStation', 'e8fc2123-2aaf-46ff-ad79-51d4002a1ef3'),
                            ('SearchDate','2017/02/22'),
                            ('SearchTime', '21:30'),
                            ('SearchWay', 'DepartureInMandarin'),
                            ])

#get the page
req = Request(url)
req.add_header('Origin','http://www.thsrc.com.tw')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')

handler = urlopen(req, data=postDate.encode())
html = handler.read().decode()
handler.close()


#save the page
with open('/Users/mac/Desktop/pacong/3_with_posts','w') as f :
    f.write(html)

