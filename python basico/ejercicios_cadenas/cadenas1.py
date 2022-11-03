cadena = input("Introduce una cadena")
if cadena == (cadena[::1].lower()).strip():
    print("si es palindromo")
else:
    print("No es un palindromo")