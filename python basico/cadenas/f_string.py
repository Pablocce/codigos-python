manzanas = int(input("Introduce cuantos kilos de manzanas compras: "))
peras = int(input("Introduce cuantos kilos de peras compras: "))
melocoton = int(input("Introduce cuantos kilos de melocotones compras: "))
manzanas = manzanas * 1.8
peras = peras *2.4
melocoton = melocoton * 4.2
total = manzanas + peras + melocoton
iva = total * 8 / 100
totalconiva = total + iva
print(f"manzanas (1,80€/kg):")