#Hacer un programa en python que cree las tablas necesarias para hacer el programa de la fruteria.
import psycopg2
sql = """create table if not exists frutas(
	nombre varchar(15) primary key,
	kilos int not null,
	precio decimal not null
);
create table  if not exists usuarios(
	nombre_usuario varchar(10) primary key,
	contraseña varchar(10) not null,
	tienda varchar(15) not null
);
CREATE TABLE IF NOT EXISTS registroPedidos (
	id_pedido SERIAL PRIMARY KEY,
	usuario VARCHAR(10) NOT NULL,
    nombre_fruta varchar(15) NOT NULL,
	cantidad_kilos INT NOT NULL,
	precio DECIMAL NOT NULL
);
"""


try:
    conn = psycopg2.connect(
        host="localhost",
        database="fruteria",
        user="postgres",
        password="Curso2023",
        port="5432"
    )
    print("Conexión correcta")
    
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    print("realizado correctamente jeje")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print("Database conection closed")