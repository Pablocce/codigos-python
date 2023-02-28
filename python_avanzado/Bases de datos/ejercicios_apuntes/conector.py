import psycopg2
conn=None
try:
    #creamos conexión
    conn = psycopg2.connect(
    host="192.168.1.240",
    database="midb",
    user="admin",
    password="#!Temporal.2022")
    #creamos un cursor
    cur = conn.cursor()
    #ejecutamos la query
    cur.execute('SELECT version()')
    #extraemos la primera linea
    print(cur.fetchone())
    #cerramos el cursor
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
