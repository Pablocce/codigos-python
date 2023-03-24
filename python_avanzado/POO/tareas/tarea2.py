import psycopg2
import csv
from tabulate import tabulate

class Conexion():
    def conectarse(self):       #Funcion de la clase para crear la conexion y devolverla
        conn = None
        try:
            conn = psycopg2.connect(host="localhost", user="python",password="odoo", port="5432", database="prueba")           
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return conn

class CSV():
    def leerDatos(self,nombre):     #Como parametro le pasamos la string con el nombre del fichero que queramos leer. Vamos a leer datos del CSV
        with open(nombre, 'r', encoding="utf8") as fich:
            next(fich) #Quitamos las cabeceras del CSV
            next(fich) #Tambien nos saltamos el hueco en blanco que se ha quedado
            contenido = csv.reader(fich, delimiter=";")
            lista = list(contenido)
        
        print("\n\nLISTA DEL CSV CREADO\n")      
        print(tabulate(lista, colalign="center", headers=["Año", "Distrito", "Col. Doble", "Col. Multiple", "Choque Obj Fijo", "Atropello", "Vuelco", "Caida motocicleta", "Caida ciclomotor", "Caida bicicleta", "Caida bus", "Otras causas"]))


    def escribirDatos(self,nombre,cursor):
        fichero = open(nombre, 'w', encoding="utf8")   
        writer = csv.writer(fichero, delimiter=";")
        writer.writerow(["Año", "Distrito", "Colision Doble", "Colision Multiple", "Choque Obj Fijo", "Atropello", "Vuelco", "Caida motocicleta", "Caida ciclomotor", "Caida bicicleta", "Caida Viajero bus", "Otras causas"])   
        cursor.copy_to(fichero, 'accidentes', sep=";", null=" ") #Vamos a trabajar con la tabla accidentes creada anteriormente
        print("\nDatos insertados en el CSV:", nombre, "\n")
        fichero.close()


class ClaseHija(CSV, Conexion):                 #Clase vacía que hereda los métodos de CSV y Conexion
    pass


        
a = ClaseHija()
conn = None
try:
    conn = a.conectarse()                                   #Método de la clase Conexión
    cur = conn.cursor()
    a.escribirDatos('Accidentes.csv', cur)                  #Método de la clase CSV
    a.leerDatos('Accidentes.csv')                           #Método de la clase CSV
    
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('\n\nDatabase connection closed.')