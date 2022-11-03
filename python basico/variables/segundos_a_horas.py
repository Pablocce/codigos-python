entrada_segundos = int(input("Introduce los segundos a transformar: "))
segundos = entrada_segundos % 60
minutosaux = int(entrada_segundos / 60)
minutos = minutosaux % 60
hora = int(minutosaux / 60)
print("Formato horas, minutos y segundos")
print(hora,":",minutos,":",segundos)