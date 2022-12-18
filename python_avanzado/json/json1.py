import  json

path = (r"C:\Users\pablo\Documents\GitHub\codigos-python\python_avanzado\json\metallica2.json")

#with open(path, "r", encoding="utf-8") as f:
#    json_string = f.read()

#print(json_string)
#print(type(json_string))

with open(path, encoding="utf-8") as file:
    data = json.load(file)


for dato in data["album"]:
    print("Nombre", dato["name"])
