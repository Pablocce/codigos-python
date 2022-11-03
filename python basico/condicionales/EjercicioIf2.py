numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))


if numero1 > numero2 and numero1 > numero3:   #Condiciones para numero 1 mayor
    if numero2 > numero3:
        print(numero1, numero2, numero3)
    else:
        print(numero1,numero3,numero2)
else: 
    if numero2 > numero1 and numero2 > numero3: #Condiciones para numero 2 mayor
        if numero1>numero3:
            print(numero2,numero1,numero3)
        else:
            print(numero2,numero3,numero1)
    else:                                        #Condiciones para numero 3 mayor
        if numero1>numero2:
            print(numero3,numero1,numero2)
        else:
            print(numero3,numero2,numero1)