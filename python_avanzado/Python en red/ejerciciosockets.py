import urllib.request, urllib.parse, urllib.error

url="http://media1.giphy.com/media/7FgI6zmKl0qQt41Snj/giphy.gif?"
img=urllib.request.urlopen(url).read()
with open("fichero.gif",'wb') as f:
    f.write(img)

url="http://media0.giphy.com/media/BBkKEBJkmFbTG/giphy.gif?"
img=urllib.request.urlopen(url).read()
with open("fichero2.gif",'wb') as f:
    f.write(img)

url="http://img.asmedia.epimg.net/resizer/hzyrX0XCnJEw5Iv4jkV-swgkPbw=/644x362/cloudfront-eu-central-1.images.arcpublishing.com/diarioas/FESQVRBJPVERHJSMUUFDUUEZBU.jpg"
img=urllib.request.urlopen(url).read()
with open("fichero3.jpg",'wb') as f:
    f.write(img)

#El ultimo link no funciona!