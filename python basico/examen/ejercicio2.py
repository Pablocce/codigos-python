from examen import espanol_ingles, ingles_frances, frances_aleman


def español_ingles():
    palabras = input("Introduce palabras en español delimitadas por comas: ")
    lista = []
    lista = palabras.split(",")
    aux = len(lista)
    for x in lista:
        if x in espanol_ingles:
            print(espanol_ingles.get(x))
        else:
            x.replace(x,"*")
            print(x)

def español_frances():
    palabras = input("Introduce palabras en español delimitadas por comas: ")
    lista = []
    lista = palabras.split(",")
    aux = len(lista)
    for x in lista:
        if x in espanol_ingles:
            aux = espanol_ingles.get(x)
            print(ingles_frances.get(aux))
        else:
            print("No existe")

def frances_español():
    palabras = input("Introduce palabras en francés delimitadas por comas: ")
    lista = []
    lista = palabras.split(",")
    aux = {y: x for x, y in ingles_frances.items()}  #ingles frances invertido
    aux2 = {y: x for x, y in espanol_ingles.items()} # español ingles invertido
    print(aux)
    print(aux2)
    for x in lista:
        if x in aux:
            palabraIngles = aux.get(x)
            if palabraIngles in aux2:
                print(aux2.get(palabraIngles))
            else:
                print("No esta")


def menu():
    seleccion = ""
    while seleccion != 4:
        print("Traducir español a ingles pulse 1")
        print("Traducir español a frances pulse 2")
        print("Traducir frances a español pulse 3")
        print("Salir pulse 4")
        seleccion = int(input("Introduce una opción: "))
        if seleccion == 1:
            español_ingles()
        elif seleccion == 2:
            español_frances()
        elif seleccion == 3:
            frances_español()
        elif seleccion == 4:
            print("Adios")
        else:
            print("Introduce un numero valido")
        

menu()