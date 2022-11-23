import leercorreo
import re

aux = leercorreo.correos()
patron = ("([a-zA-Z0-9]\S*)@")
usuario = re.findall(patron, leercorreo.correos())
for user in usuario:
    print(user)
 
