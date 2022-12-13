import xml.etree.ElementTree as ET
path = (r"C:\Users\pablo\Documents\GitHub\codigos-python\python_avanzado\xml\clima.xml")
#We can import this data by reading from a file:
tree = ET.parse(path)
root = tree.getroot()

#Calculo temperatura mínima media del año
x = 0
y = 0
mediaMinima = 0
media = 0
for child in root:
    mediaMinima += float(root[x][4].text)
    media += float(root[x][3].text)
    x += 1
    y += 1
print("Temperatura mínima media", mediaMinima/y)
print("Temperatura media",media/y)

x = 0
cont = 0
for child in root:
    if float(root[x][8].text) > 1.5:
        print(root[x][1].text, "radiacion: ", root[x][8].text)
        cont += 1
    x += 1
print("Días en los que se supero 1,5 en radiación:",cont)
