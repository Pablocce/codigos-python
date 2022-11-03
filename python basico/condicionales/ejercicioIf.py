import sys
if len(sys.argv) ==  3 :
    if sys.argv[2] == "r" or "RAIZ"  or "raiz":
        print(int(sys.argv[1])**(0.5))
    else: 
        if sys.argv[2] == "cuadrado" or "CUADRADO":
            print("si")
else:
    if len(sys.argv) == 4:
        if sys.argv[3] == "sumar":
            sys.argv[3] = "+"
        if sys.argv[3] == "restar":
            sys.argv[3] = "-"
        if sys.argv[3] == "multiplicar":
            sys.argv[3] = "*"
        if sys.argv[3] == "dividir":
            sys.argv[3] = "/"
        aux = str(sys.argv[1] + sys.argv[3]+ sys.argv[2])
        print(eval(aux))
    else:
        print("Argumentos invalidos")
    


