# Task 1: Setting Up a Python Virtual Environment and Installing Packages
# This step should be done in your terminal/command line interface.
# Command to create a virtual environment: python -m venv myenv
# Command to activate the virtual environment:
# On Windows: myenv\Scripts\activate
# On macOS/Linux: source myenv/bin/activate
# Command to install the requests package: pip install requests

import requests

# Task 2: Fetching Data from the Pokémon API
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

def display_pokemon_info(pokemon_data):
    name = pokemon_data['name']
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    print(f"Name: {name}")
    print("Abilities:")
    for ability in abilities:
        print(f"- {ability}")

# Fetching and displaying data for Pikachu
pikachu_data = fetch_pokemon_data("pikachu")
display_pokemon_info(pikachu_data)

# Task 3: Analyzing and Displaying Data
def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data_list = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon_data in pokemon_data_list:
    display_pokemon_info(pokemon_data)

average_weight = calculate_average_weight(pokemon_data_list)
print(f"Average Weight: {average_weight} decigrams")
