#Haz un programa .py que cree una clase vacia y vaya añadiendo metodos e instancias. Al menos dos metodos y dos variables.

class MiClase1:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    def hobbies(self):
        print("Me gusta mucho programar")
    def despedirse(self):
        print("Adiós, ¡hasta luego!")

# Crear una instancia de la clase MiClase1
mi_instancia = MiClase1("Pablo", 19)

# Llamar a los métodos de la instancia
mi_instancia.saludar()
mi_instancia.hobbies()
mi_instancia.despedirse()

print("-------------------------------------------------------------------------------")


#ahora sin tocar la clase

class MiClase1:
    pass

# Crear una instancia de la clase MiClase
mi_instancia = MiClase1()

# Añadir variables a la instancia
mi_instancia.nombre2 = "Juan"
mi_instancia.edad2 = 25

# Añadir métodos a la instancia
def saludar(self):
    print(f"Hola, mi nombre es {self.nombre2} y tengo {self.edad2} años.")

def hobbies(self):
    print("Me gusta mucho programar")

def despedirse(self):
    print("Adiós, ¡hasta luego!")

mi_instancia.saludar = saludar
mi_instancia.hobbies = hobbies
mi_instancia.despedirse = despedirse

# Llamar a los métodos de la instancia
mi_instancia.saludar(mi_instancia)
mi_instancia.hobbies(mi_instancia)
mi_instancia.despedirse(mi_instancia)