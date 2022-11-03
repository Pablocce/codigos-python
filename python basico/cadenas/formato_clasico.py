nombre = (input("Introduce el nombre: ")) #no indico str ya que no hace falta
apellido1 = input("Introduce el primer apellido: ")
apellido2 = input("Introduce el segundo apellido: ")
telefono = input("Introduce el número de telefono: ")
numero = float(input("Introduce un número para el cálculo: "))
numero = numero**(0.5)
print("%s %s %s, número de telefono: %s, raiz 1: %.2f, raiz 2: %.5f" %(nombre,apellido1,apellido2,telefono,numero,numero))

