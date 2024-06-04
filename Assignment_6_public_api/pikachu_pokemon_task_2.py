import requests
from requests.exceptions import RequestException

pikachu_url = "https://pokeapi.co/api/v2/pokemon/pikachu"


def display_pokemon_name_and_ability():

    try:
        response = requests.get(pikachu_url)
        data = response.json()

        if response.status_code == 200:
            print(f"Pokemon Name is: {data['name']}")
            pokemon_abilities = []
            for ability in data.get('abilities'):
                pokemon_abilities.append(ability['ability']['name'])
            print("Pikachu abilities are: ", ', '.join(pokemon_abilities))

        else:
            print("Error: ", response.status_code)
    except RequestException as e:
        print(f"Exception while getting data. Error: {e}")


display_pokemon_name_and_ability()
