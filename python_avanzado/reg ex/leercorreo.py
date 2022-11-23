import urllib.request

def correos():
    url="http://www.py4inf.com/code/mbox-short.txt"


    with urllib.request.urlopen(url) as web:
        texto = web.read()
    # LAs web estan en byte hay que transformalas en string
    return texto.decode("utf-8")


