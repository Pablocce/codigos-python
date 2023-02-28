import psycopg2
import csv

conn=None
sql =("""
CREATE TABLE if not exists pisos(
url VARCHAR(45),
direccion VARCHAR(100),
precio INT,
habitaciones VARCHAR(150),
tamaño VARCHAR(150),
otros VARCHAR(100),
telefono VARCHAR(15),
id SERIAL PRIMARY KEY
)
""")


try:
    conn = psycopg2.connect(
        host="localhost",
        database="db_pisos",
        user="postgres",
        password="Curso2023",
        port="5432"
    )
    print("Conexión correcta")
    
    cur = conn.cursor()
    cur.execute(sql)
    cur.execute("truncate table pisos")
    conn.commit()
    

    print("Leyendo csv pisos...")
    with open(r"C:\Users\pablo\Documents\GitHub\codigos-python\python_avanzado\Bases de datos\ejercicios_tarea\Pisos_CSV_to_DB\2020-04-03-madrid-madrid-alquiler.csv",'r', encoding='utf-8') as archivo_csv:
        reader = csv.reader(archivo_csv)
        next(reader) #lo usamos para saltar la cabecera
        

        for fila in reader:
            url = fila[0]
            direccion = fila[1]
            precio = int(fila[2].replace('€', '').replace('/mes', ''))
            habitaciones = fila[3]
            tamano = fila[4]
            otros = fila[5]
            telefono = fila[6]
            cur.execute("""INSERT INTO pisos(url, direccion, precio, habitaciones, tamaño, otros, telefono)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
            """,(url,direccion,precio,habitaciones,tamano,otros,telefono))
            conn.commit()
    cur.close()
    print("realizado correctamente jeje")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print("Database conection closed")
