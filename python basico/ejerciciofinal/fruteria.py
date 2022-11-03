from operator import truediv

frutas = []
precios = []
cantidad = []


ticketProductos = []
ticketPrecios = []
ticketCantidad = []

def añadirProducto():
    print("Quieres añadir un producto nuevo? Introduce 1")
    print("Quieres modificar un producto existente? Introduce 2")
    print("Quieres volver al menu? Introduce salir")
    opcion = int(input("Introduce una opción: "))
    if opcion == 1:
        fruta = input("Introduce el nombre de la fruta: ")
        precio = float(input("Introduce el precio de la fruta: "))
        kilo = float(input("Introduce los kilos disponibles: "))
        frutas.append(fruta)
        precios.append(precio)
        cantidad.append(kilo)
        añadirProducto()
    elif opcion == 2:
        fruta = input("Introduce el nombre de la fruta que quieres buscar")
        if fruta in frutas:  #recorre la lista en busca de la fruta
            index = frutas.index(fruta)
            print("Cambiar precio : 1 \n Cambiar cantidad en kilos : 2")
            opcion = int(input("Introduce una opcion para cambiar"))
            if opcion == 1:
                print("Precio actual: ", precios[index])
                precio = float(input("A que precio quieres cambiar el producto"))
                precios[index] = precio
                print("Precio de ", frutas[index], "cambiado a: ", precio)
            if opcion == 2:
                print("Cantidad actual del producto", frutas[index], cantidad[index], "KG")
                kilo = float(input("Introduce la cantidad nueva del producto: "))
                cantidad[index] = kilo
                print("Cantidad del producto ", fruta[index], "cambiada a: ", cantidad[index])
        else:
            print("No existe esa fruta")
        añadirProducto()
    elif opcion == "salir":
        print("Volviendo al menu")
        menu()
    else:
        print("Opción invalida")
        añadirProducto()

def ventas():
    print("ventas")

def buscarProducto():
    print("busqueda")

def anotarProducto():
    print("si")


def crearTicket():
    print("Tickets")
    print("Opciones: \n 1. Añadir al carrito \n 2. Finalizar compra \n 3. Salir")
    
    opcion = int(input("Introduce una opcion (numero): "))
    if opcion == 1:
        for x in range(frutas):
            print(x+1,": "+ frutas[x])
        product = int(input("Marca un producto (introduce su número)"))
        ticketProductos.append(product)
        index = frutas.index(product-1)
        ticketPrecios.append(index)
        cant = int(input("Cuanta cantidad del producto quieres retirar?"))
        if cantidad[index] > cant:
            ticketCantidad.append(cant)
            cantidad[index] = cantidad[index] - cant
        crearTicket()
    elif opcion == 2:
        print("----------------------Ticket final-------------------------")
        for x in range(len(ticketProductos)):
            print(ticketProductos[x], "cant: ", ticketCantidad[x],"         ", ticketPrecios[x])
            cantidad[x] =  int (cantidad[x]) - int(ticketCantidad[x])
            sumaTotal =  sumaTotal + int(ticketPrecios[x] * int(ticketCantidad[x]))
        print("Total sin iva: ", sumaTotal - sumaTotal/100 * 0.08)
        print("Total con iva: ", sumaTotal)
    elif opcion == 3:
        menu()
    else:
        print("Opción no valida")
        crearTicket()




        

def menu():
    print("Bienvenido al programa de gestión de la fruteria")
    print("Opciones: ")
    print("1- Añadir producto")
    print("2- Ventas")
    print("3- Buscar producto")
    print("4- Crear ticket")
    print("Salir")
    
    salir = False
    while salir == False:
        opcion = int(input("Introduce una opción: "))
        if opcion ==1:
            añadirProducto()
        elif opcion ==2:
            ventas()
        elif opcion ==3:
            buscarProducto()
        elif opcion ==4:
            crearTicket()
        else:
            print("Opcion no valida")

menu()