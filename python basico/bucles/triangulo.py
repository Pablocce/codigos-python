num = int(input("inserta un numero: "))
cont=0
while cont<=num:
    if cont%2 == 0:
        print(" ")
        cont = cont+1
    elif cont%2 != 0:
        if num == 1:
            print(cont)
            cont = cont+1
        else:
            num1 = cont
            while num1>=1:
                if num1%2 == 0:
                    print(" ",end="")
                    num1=num1-1
                else:
                    print(num1,end="")
                    num1=num1-1
            cont=cont+1