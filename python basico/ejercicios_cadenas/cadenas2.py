import variables

#primer apartado
num = variables.ejercicio1.find("0.8475")    #detectar posicion
print("El numero es:",float(variables.ejercicio1[num::]))
print("-------------------------------------------------------------")

#segundo apartado
ubiPlatanos = variables.ejercicio2.find("platanos peso=")
pesoPlatanos = float(variables.ejercicio2[ubiPlatanos+14:ubiPlatanos+18])
ubiPlatanos = variables.ejercicio2.find("kilo platano=")
precioPlatanos = float(variables.ejercicio2[ubiPlatanos+13:ubiPlatanos+17])
print("Los platanos cuestan:",precioPlatanos * pesoPlatanos)

ubiPera = variables.ejercicio2.find("peras peso=")
pesoPera = float(variables.ejercicio2[ubiPera+11:ubiPera+15])
ubiPera = variables.ejercicio2.find("kilo peras=")
precioPera = float(variables.ejercicio2[ubiPera+11:ubiPera+15])
print("Las peras cuestan:",precioPera * pesoPera)
print("-------------------------------------------------------------")

aux = variables.ejercicio3.split("#")
print(aux[1])
print(aux[2])
print(aux[3])
