import requests
from requests.exceptions import RequestException

pokemon_url = 'https://pokeapi.co/api/v2/pokemon/'


def fetch_pokemon_data(pokemon_name):
    url = pokemon_url + pokemon_name

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error in status code. code: {response.status_code}")
            return {}
    except RequestException as e:
        print(f"Error in getting pokemon data. Error: {e}")


def calculate_average_weight(pokemon_names_list):
    average_weights = []

    for pokemon in pokemon_names_list:
        data = fetch_pokemon_data(pokemon)

        if len(pokemon) == 0:
            print("Empty data returned")
        else:
            print(f"Pokemon name is: {data['name']} and it's abilities are: ", end='')
            abilities = [ability['ability']['name'] for ability in data['abilities']]
            print(', '.join(abilities))
            average_weights.append(data['weight'])

    print(f"average weight of pokemons {', '.join(pokemon_names_list)} is: {sum(average_weights)/len(average_weights)}")


pokemon_names = ["pikachu", "bulbasaur", "charmander"]

calculate_average_weight(pokemon_names)
