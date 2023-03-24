import csv

class Alumnos:
    def __init__(self, nombre, dni, notas):
        self.__nombre = nombre
        self.__dni = dni
        self.__notas = notas
        self.__media = sum(notas) / len(notas) #media tres evaluaciones
    #como hemos hecho privados los atributos creamos unos getters como en java para las demás funciones
    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def get_notas(self):
        return self.__notas

    def get_media(self):
        return self.__media
    

class GestionarAlumnos:
    def __init__(self):
        self.alumnos = [] #lo almacenamos el listas

    def insertar(self):
        nombre = input("Introduce nombre alumno: ")
        dni = input("Introduce dni alumno: ")
        notas = [] #lista de las 3 notas
        for x in range(3): #tres evaluaciones
            nota = float(input("Introduce la nota de la evaluación: "))
            notas.append(nota)
        alumno = Alumnos(nombre,dni,notas)
        self.alumnos.append(alumno)
        

    def mostrarAlumnos(self):
        print("-------------------------------------------------")
        print("Listado de alumnos:")
        for alumno in self.alumnos:
            print("Nombre --> ", alumno.get_nombre()," DNI --> ", alumno.get_dni(), " Notas --> ", alumno.get_notas(), " Nota media (3 evaluaciones) --> ", alumno.get_media()) 

    def buscarAlumnoDNI(self,dni):
        print("-------------------------------------------------")
        print("Apartado buscar alumnos por dni")
        x = 0
        for alumno in self.alumnos:
            if alumno.get_dni() == dni:
                print("Nombre --> ", alumno.get_nombre()," DNI --> ", alumno.get_dni(), " Notas --> ", alumno.get_notas(), " Nota media (3 evaluaciones) --> ", alumno.get_media()) 
                x = x + 1
        if x == 0:
            print("No existe ningun alumno con el dni --> ", dni)     
    
    def exportarCSV(self):
        print("-------------------------------------------------")
        print("Exportando datos a fichero csv ...")
        with open("alumnos.csv", mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"')
            writer.writerow(['Nombre', 'DNI', 'Nota 1', 'Nota 2', 'Nota 3', 'Media'])
            for alumno in self.alumnos:
                writer.writerow([alumno.get_nombre(), alumno.get_dni(), *alumno.get_notas(), alumno.get_media()])

                
gestor = GestionarAlumnos()
opcion = 0
while opcion !=  5:
    print("\n\nBienvenido al programa de gestión de alumnos")
    print("Si quiere introducir un nuevo alumno escriba 1")
    print("Si quiere ver el listado de alumnos escriba 2")
    print("Si quiere buscar un alumno por su dni escriba 3")
    print("Si quiere exportar el listado de alumnos a un fichero CSV escriba 4")
    print("Para salir introduzca 5")
    opcion = int(input("Introduce opcion:"))
    if opcion == 1:
        gestor.insertar()
    elif opcion == 2:
        gestor.mostrarAlumnos()
    elif opcion == 3:
        dni = input("Introduce el dni del alumno a buscar: ")
        gestor.buscarAlumnoDNI(dni)
    elif opcion == 4:
        gestor.exportarCSV()
    else:
        print("Introduzca una opcion valida")


