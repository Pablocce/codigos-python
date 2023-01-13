import urllib.request
import json
import csv

def get_jokes(num_bromas):
    chistes = []
    for i in range(num_bromas):
        url = f"https://api.chucknorris.io/jokes/random"
        req = urllib.request.Request(url, headers={"User-Agent": ""})
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read().decode())
        chistes.append(data["value"])
    return chistes

chistes = get_jokes(5)

with open("chistes_chuck.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Chistes"]) # Añade la cabecera
    writer.writerows([[j] for j in chistes]) # escribe las filas con los chistes
