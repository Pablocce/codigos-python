import urllib.request, urllib.parse, urllib.error
url="https://busybox.net/downloads/busybox-1.35.0.tar.bz2"
iso=urllib.request.urlopen(url)
tamano=0
with open("busybox-1.35.0.tar.bz2",'wb') as f:
    while True:
        #leemos 100000 caracteres cada vez
        datos=iso.read(100000)
        if len(datos)<1:break
        tamano+=len(datos)
        f.write(datos)
