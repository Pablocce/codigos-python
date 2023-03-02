class Nombre:
    def __init__(self,nombre = ''):
        self.nombre=nombre
    def __str__(self):
        d=f'El nombre del objecto es {self.nombre.upper()}'
        return d

a = Nombre('Juan')
print(a)