import os
os.path.realpath('.')

f = open('texto.txt', 'r')
cadena = f.read()
f.close()
print(cadena)