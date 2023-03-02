#Crear un fichero csv que tenga frutas, precio, kilos
#Leer el fichero csv y e insertarlo en la base de datos con executemany y una query parametrizada
import psycopg2
import csv


conn=None
try:
    conn = psycopg2.connect(
        host="localhost",
        database="fruteria",
        user="postgres",
        password="Curso2023",
        port="5432"
    )
    print("Conexión correcta")
    print("Leyendo csv frutas...")
    with open(r"C:\Users\pablo\Documents\GitHub\codigos-python\python_avanzado\Bases de datos\executemany\frutas.csv",'r', encoding='utf-8') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
    # Crear una lista de diccionarios a partir del objeto lector CSV
        data = []
        for row in reader:
            tupla = (row['nombre'], row['precio'],row['kilos'])
            data.append(tupla)
    
    cur = conn.cursor()
    query = "insert into frutas (nombre,precio,kilos) values(%s,%s,%s)"
    cur.executemany(query,data)
    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print("error: " , error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')

