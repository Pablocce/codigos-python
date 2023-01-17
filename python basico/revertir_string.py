def revertir_string(cad):
    cadena_invertida = ""
    for letra in cad:
        cadena_invertida = letra + cadena_invertida
    print(cadena_invertida)
    return cadena_invertida
    
cad = input("Introduce el string a invertir: ")
revertir_string(cad)