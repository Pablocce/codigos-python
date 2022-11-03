nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))
direccion = input("Introduce la dirección: ")
telefono = input("Introduce el telefono: ")

dicc = {"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telefono}
print(dicc["nombre"], "tiene", dicc["edad"], " años, vive en ", dicc["direccion"],"y su numero de teléfono es",dicc["telefono"] )