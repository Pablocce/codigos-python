import psycopg2
data = [] #va a almacenar los valores para despues poder hacer el execute many


def menu():
    print("Opciones: \n 1--> Crear pedidos o finalizar pedidos \n 2--> Inventario pedidos \n 3--> salir")
    opcion = int(input("Introduzca una de las dos opciones (el número): "))
    if opcion == 1:
        crearPedidos()
    elif opcion == 2:
        inventarioPedidos()
    elif opcion == 3:
        exit()
    else:
        print("No has introducido una opcion valida \n \n")
    menu()


def crearPedidos():
    opcion = int(input("Si desea crear un pedido pulse 1, si quiere finalizarlo pulse 2"))
    if opcion == 1:
        print("Creación de pedido: ")
        bandeja = int(input("Introduce el tamaño de la bandeja: \n 1 para pequeña \n 2 para mediana \n 3 para grande\n que tamaño quieres: "))
        print("Elección de ingredientes: \n SI NO QUIERES INTRODUCIR NINGUNO ESCRIBE 0")
        ternera = int(input("Cuanta ternera quiere añadir?"))
        pollo = int(input("Cuanta pollo quiere añadir?"))
        patatas = int(input("Cuanta patatas quiere añadir?"))
        pescado = int(input("Cuanta pescado quiere añadir?"))
        huevos = int(input("Cuanta huevos quiere añadir?"))
        bacon = int(input("Cuanta bacon quiere añadir?"))
        lechuga = int(input("Cuanta lechuga quiere añadir?"))
        cantidadIngredientes = ternera + pollo + patatas + pescado + huevos + bacon + lechuga
        print("Ha seleccionado un total de ", cantidadIngredientes, " ingredientes")
        if cantidadIngredientes > 2:
            extraIngredientes = (cantidadIngredientes - 2) * 2
        else:
            extraIngredientes = 0
        if bandeja == 1:
            precio = 8 + extraIngredientes
            tamaño = "pequeña"
        elif bandeja == 2:
            precio = 12 + extraIngredientes
            tamaño = "mediana"
        elif bandeja == 3:
            precio = 18 + extraIngredientes
            tamaño = "grande"
        lista = [tamaño,precio,ternera,pollo,patatas,pescado,huevos,bacon,lechuga]
        #data.append([tupla])
        #print(data)
        
        data.append(lista)
        print(data)
    elif opcion ==2:
        print("Finalizando pedido")
        try:
            cur = conn.cursor()
            sql = """INSERT INTO tbpedidos
                    (bandeja, precio, ternera, pollo, patatas, pescado, huevos, bacon, lechuga)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            print(data)
            cur.executemany(sql,data)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("error: " , error)
        cur.close()


def inventarioPedidos():
    opcion = 0
    while opcion != 4:
        print("Elige una opción: \n 1--> Número de pedido y recaudación \n 2--> Uso de ingredientes \n 3--> Tamaño bandejas \n 4--> Salir")
        opcion = int(input("Introduce una opción(el número): "))
        if opcion == 1:
            cur = conn.cursor()
            cur.execute("select count(id) as pedidos, sum(precio) as beneficio from tbpedidos") 
            row = cur.fetchone()
            print("Pedidos realizados--> ", row[0], " Beneficio obtenido--> ", row[1], "\n \n")
            cur.close()
        elif opcion ==2:
            cur = conn.cursor()
            cur.execute("select sum(ternera) as ternera, sum(pollo) as pollo, sum(patatas) as patatas, sum(pescado) as pescado, sum(huevos) as huevos, sum(bacon) as bacon, sum(lechuga) as lechuga from tbpedidos")
            row = cur.fetchone()
            print("Ternera -->", row[0], "Pollo -->", row[1], "Patatas -->", row[2], "Pescado -->", row[3], "Huevos -->", row[4], "Bacon -->", row[5], "Lechuga -->", row[6],"\n\n")
            cur.close()
        elif opcion ==3:
            cur = conn.cursor()
            cur.execute("select bandeja from tbpedidos")
            row = cur.fetchall()
            pequeñas = 0
            medianas = 0
            grandes = 0
            for tupla in row:
                bandeja = tupla[0]
                if bandeja == "pequeña":
                    pequeñas += 1
                elif bandeja == "mediana":
                    medianas += 1
                elif bandeja == "grande":
                    grandes += 1
            print("Bandejas pequeñas --> ", pequeñas, " Bandejas medianas --> ", medianas, " Bandejas grandes --> ", grandes, "\n")
            cur.close()
        elif opcion == 4:
            print("Saliendo al menú principal")




try:
    conn = psycopg2.connect(
        host="localhost",
        database="restaurante",
        user="postgres",
        password="Curso2023",
        port="5432"
    )

    print("Conexión correcta")
    
    sql = """create table if not exists tbpedidos(
	id serial primary key,
	bandeja varchar(10) not null,
	precio decimal not null,
	ternera int,
	pollo int,
	patatas int,
	pescado int,
	huevos int,
	bacon int,
	lechuga int
    );"""
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    menu()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print("Database conection closed")