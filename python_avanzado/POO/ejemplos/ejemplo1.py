#Función

def sumarUno(num):
    return num+1

class Prueba:
    x=0
    #metodo
    def aumentar(self):
        self.x = sumarUno(self.x)

a=Prueba()
a.aumentar()
print(a.x)