frase = ""


def letras():
    mayusculas = 0
    minusculas = 0
    signos = 0
    espacio = 0
    for letra in frase:
        if letra == letra.upper() and letra.isalpha() == True:
            mayusculas += 1
        elif letra == letra.lower() and letra.isalpha() == True:
            minusculas += 1
        elif letra.isalpha() == False and letra != " ":
            signos += 1
        else:
            espacio += 1
    print("La cadena tiene " , mayusculas , " mayusculas")
    print("La cadena tiene " , minusculas , " minusculas")
    print("La cadena tiene " , signos , " signos")
    print("La cadena tiene " , espacio , " espacios")

def contar():
    aux = {}
    for i in frase:
        aux[i] = aux.get(i, 0) + 1
    print(aux)



salir = False
while salir != True:
    frase = input("Introduce una frase ")
    if frase == "fin":
        salir = True
    else:
        letras()
        contar()
