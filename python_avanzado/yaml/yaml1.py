import yaml


path = (r"C:\Users\pablo\Documents\GitHub\codigos-python\python_avanzado\yaml\pokemones.yaml")
#Abrimos el archivo YAML
with open(path,"r") as file:
    datos = yaml.safe_load(file)
    
for pokemon in datos["pokemones"]:
    print(pokemon["nombre"])