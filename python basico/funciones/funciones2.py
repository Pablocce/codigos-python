opcion = input("Opciones: cuadrado, piramide, rectangulo, rombo o salir")

def cuadrado():
    altura = int(input("Introduce la altura"))
    base = int(input("Introduce la base"))
    caracter = str(input("Introduce el caracter"))
    for x in range(1,base+1):
        for y in range(1, altura+1):
            print(caracter, end= " ")
        print(" ")

def piramide():
    altura = int(input("Introduce la altura"))
    caracter = str(input("Introduce el caracter"))
    for i in range(1, altura+1):
        for j in range(altura - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            print(caracter, end="")
        print()
    for i in range(altura):
        for j in range(i):
            print(" ", end="")
        for j in range(altura - i):
            print(caracter, end="")
        print()


piramide()


#if opcion == "salir":
#    exit()
