import requests


url_api = "https://pokeapi.co/api/v2/pokemon"
def main():
    print("Bienvenido a la biblia de los pokemons")
    print("Api: ")
    print("----------------------------------------------------")
    pokemon_name = input("Introduce el nombre del pokemon: ")
    pokemon_data_url = url_api + pokemon_name
    data = get_pokemon_data(pokemon_data_url)

    pokemon_type = [types['type']['name'] for types in data['types']]
    print(data)
    print(pokemon_type)

def get_pokemon_data(url_pokemon=''):
    pokemon_data = {
        "name" : '',
        "height": '',
        "habilities": '',
        "types": '',
        "weight": ''
    }

    response = requests.get(url_pokemon)

main()

