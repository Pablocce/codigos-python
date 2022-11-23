def insertar(alumnos):
    nombre = input("Introduce el nombre del alumno ")
    dni = input("Introduce el dni del alumno ")
    apellido = input("Introduce el apellido del alumno ")
    clase = input("Introduce la clase del alumno ")
    alumnos[dni] = nombre, apellido, clase
    return(alumnos)

def mostrar(alumnos):
    auxDNI = input("Introduce el dni a consultar ")
    if auxDNI in alumnos:
        print(alumnos[auxDNI])
    else:
        print("No existe ningun alumno con ese dni")
    menu()

def eliminar(alumnos):
    auxDNI = input("Introduce el dni del alumno que quieres borrar: ")
    if auxDNI in alumnos:
        alumnos.pop(auxDNI)
        print("Alumno borrado")
    else:
        print("No existe el valor")
    menu()



def menu():
    alumnos = {}
    opcion = ""
    print("Programa de gestión de alumnos")
    while opcion !="4":
        print("1. insentar")
        print("2. mostrar")
        print("3. eliminar")
        opcion = int(input("Introduce una opción"))
        if opcion == 1:
            alumnos = insertar(alumnos)
        elif opcion == 2:
            mostrar(alumnos)
        elif opcion ==3:
            eliminar(alumnos)


menu()