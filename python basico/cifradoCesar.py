numeroSlides = int(input("Introduce el número de desplazamiento"))
cadena = "a"
cont = 0
while cadena != "FIN":
    cadena[cont] = str(input("Introduce una cadena"))
    cont = cont + 1
    if cadena[cont][0:] == "#":
        print("SI")
