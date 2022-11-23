from operator import truediv
import os
from time import sleep
frutas = []
precios = []
cantidad = []

#producto : [precioKg, stock] dicc

sumaTotal = 0


ticketProductos = []
ticketPrecios = []
ticketCantidad = []

productosVendidosNombres = []
productosVendidosCantidad = []
ganaciasTotales = int


def añadirProducto():
    os.system("cls")
    print("Quieres añadir un producto nuevo? Introduce 1")
    print("Quieres modificar un producto existente? Introduce 2")
    print("Quieres volver al menu? Introduce 3")
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
    elif opcion == 3:
        print("Volviendo al menu")
        menu()
    else:
        print("Opción invalida")
        añadirProducto()


def buscarProducto():
    print("Sección de buscar producto")
    seleccionProducto = input("Introduce un producto a buscar")
    if seleccionProducto in frutas:
        print("Producto encontrado")
        index = frutas.index(seleccionProducto)
        if seleccionProducto in productosVendidosNombres:
            dinero = productosVendidosCantidad * precios[index]
            print("El producto:",seleccionProducto, "Kilos vendidos: ", productosVendidosCantidad, "Kilos en stock: ", cantidad[index], " Cantidad de dinero ganado: ", dinero)
            buscarProducto()
        else:
            print("No hay datos registrados de ese producto, no hay ventas")
            buscarProducto()



def crearTicket():
    os.system("cls")
    print("Tickets")
    print("Opciones: \n 1. Añadir al carrito \n 2. Finalizar compra \n 3. Salir")
    opcion = int(input("Introduce una opcion (numero): "))
    if opcion == 1:
        aux = 0
        for x in range(len(frutas)):
            print(x+1,": "+ frutas[x], "actualmente: ", cantidad[x], " KG")
            aux = aux + 1
        if aux == 0:
            print("No hay productos disponibles actualmente")
            menu()
        product = (input("Marca un producto (nombre): "))
        index = frutas.index(product)
        cant = int(input("Cuanta cantidad del producto quieres retirar: "))
        if cantidad[index] > cant:
            ticketProductos.append(product)
            ticketPrecios.append(precios[index])
            ticketCantidad.append(cant)
            cantidad[index] = cantidad[index] - cant
            print("Producto añadido")
        else: print("Producto  no añadido")
        sleep(2)
        crearTicket()
    elif opcion == 2:
        valorTotal = 0
        print("----------------------Ticket final-------------------------")
        for x in range(len(ticketProductos)):    #Bucle for para mostrar todos los productos, cantidad y precio
            print(ticketProductos[x], "cant: ", ticketCantidad[x],"         ", ticketPrecios[x])
            aux = int(ticketCantidad[x]) * (ticketPrecios[x])
            valorTotal = valorTotal + aux
            iva = valorTotal / 100 * 0.08
        print("Total sin iva: ", valorTotal - iva)
        print("Total con iva: ", valorTotal)
        print("\n \n \n " )
        sleep(4)
        menu()
    elif opcion == 3:
        menu()
    else:
        print("Opción no valida")
        crearTicket()


def menu():
    os.system("cls")
    print("Bienvenido al programa de gestión de la fruteria")
    print("Opciones: ")
    print("1- Añadir producto")
    print("2- Buscar producto")
    print("3- Crear ticket")
    print("4- Salir")
    
    salir = False
    while salir == False:
        opcion = int(input("Introduce una opción: "))
        if opcion ==1:
            añadirProducto()
        elif opcion ==2:
            buscarProducto()
        elif opcion ==3:
            crearTicket()
        elif opcion ==4:
            salir = True
        else:
            print("Opcion no valida")
menu()