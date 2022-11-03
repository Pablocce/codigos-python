diccFruta = {}
def añadir():
    fruta = input("Introduce el nombre de la fruta")
    precio = float(input("Introduce el precio por kilo de la fruta"))
    diccFruta[fruta] = precio
    print(diccFruta)
    menu()


def consultar(diccFruta):
    fruta = input("Introduce el nombre de la fruta")
    peso = float(input("Introduce el peso de la fruta"))
    if fruta in diccFruta:
        print("precio:",diccFruta[fruta] * peso)
    else:
        print("No está registrado")

def menu():
    print("Opciones:")
    print("Opción 1:  añadir fruta")
    print("Opcion 2: buscar fruta")
    opcion = int(input("Introduzca 1 o 2: "))
    if opcion == 1:
        añadir()
    if opcion == 2:
        consultar(diccFruta)
print("Fruteria------------------------------------")
menu()