import urllib.request

url="http://data.pr4e.org/romeo.txt"
recurso_web=urllib.request.urlopen(url)
for linea in recurso_web:
    print(linea.decode().strip())