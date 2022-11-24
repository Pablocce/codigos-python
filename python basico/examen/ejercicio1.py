from time import sleep
import os


def entradaPersonal(autonomos):   #funciona
    dni = input("Introduce el dni del autonomo: ")
    entrada = input("Introduce la hora de entrada: ")
    fecha = input("Introduce la fecha formato (dd/mm/yy): ")
    horaSalida = "Aun no ha salido"
    salario = 0
    autonomos[dni] = entrada, fecha, horaSalida, salario
    return(autonomos)

def salidaAutonomos(autonomos):  #funciona
    dni = input("Introduce el dni del autonomo: ")
    if dni in autonomos:
        horaSalida = input("Introduce la hora de salida en el formado [hh:mm]")
        horaSal = int(horaSalida[:2])
        minutosSal = int(horaSalida[-2:])
        if horaSal > 24 or minutosSal > 60:
            print("Introduce una hora correcta")
            print("Volviendo al menu de registro de salida")
            salidaAutonomos(autonomos)
        else: 
            aux=list(autonomos[dni])
            horaentrada = aux[0]
            horaEnt = int(horaentrada[:2])
            minutosEnt = int(horaentrada[-2:])
            salarioHora = 10.5
            horas = horaSal - horaEnt
            minutos = minutosSal - minutosEnt * -1
            sal = ((horas * 60 + minutos)/60) * 10.5
            print(sal)
            aux2 = list(autonomos[dni])
            autonomos.pop(dni)
            autonomos[dni] = aux2[0], aux2[1], aux[2], int(aux[3]) + sal
            return (autonomos)

def buscarEmpleado(autonomos):  #funciona
    print(autonomos) #TEST
    dni = input("Introduce el dni del autonomo: ")
    if dni in autonomos:
        aux = list(autonomos[dni])
        print("El autónomo con dni: ",dni, " entró a las: ", aux[0], "salio a las: ", aux[1], " y actualmente tiene un sueldo de: " ,aux[3])
    else:
        print("No existe ese autonomo")


def estadisticas(autonomos):  #no funciona
    print("Estadisticas:")
    fechaPreguntada = input("Introduce una fecha en formato(dd/mm/yy): ")
    personasTrabajaron = 0
    auxSalario = 0
    for dni in autonomos:  
        if fechaPreguntada in autonomos:
            personasTrabajaron += 1
            auxLista = list(autonomos[dni])
            print("Entra")
            auxSalario += auxLista[3]
    print("En la fecha: ",fechaPreguntada, " trabajaron: ", personasTrabajaron, " personas")
    print("Se debe pagar: ", auxSalario)


def cargarDatos(autonomos):  #a medias, lo carga y lo mete en una variable pero no se añade a autonomos
    d = {}
    with open("datos.txt", "r") as f:
        for line in f:
            for key, item in enumerate(d):
                (key, item) = line.split()
                
    print(d)

def guardarDatos(autonomos): #funciona
    with open("datos.txt", "w") as f:
        print(autonomos, file=f)

def menu(): #funciona
    autonomos = {}
    seleccion = 0
    while  seleccion != 7:
        print("Entrada de personal escriba 1")
        print("Salida de persona escriba 2")
        print("Buscar personal escriba 3")
        print("Estadisticas escriba 4")
        print("Cargar datos escriba 5")
        print("Guardar datos escriba 6")
        print("Para salir escriba  7")
        seleccion = int(input("Introduzca una opción: "))
        if seleccion == 1:
            autonomos = entradaPersonal(autonomos)
        elif seleccion == 2:
            autonomos = salidaAutonomos(autonomos)
        elif seleccion == 3:
            buscarEmpleado(autonomos)
        elif seleccion == 4:
            estadisticas(autonomos)
        elif seleccion == 5:
            autonomos = cargarDatos(autonomos)
        elif seleccion == 6:
            guardarDatos(autonomos)
        elif seleccion == 7:
            print("Adios")
        else:
            print("Introduce un número valido")

menu()