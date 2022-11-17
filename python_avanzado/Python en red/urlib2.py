import urllib.request, urllib.parse, urllib.error

url="http://media1.giphy.com/media/COYGe9rZvfiaQ/giphy.gif?"
img=urllib.request.urlopen(url).read()
with open("fichero.gif",'wb') as f:
    f.write(img)
