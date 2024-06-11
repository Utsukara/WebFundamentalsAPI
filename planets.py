# Task 1: Setting Up a Python Virtual Environment and Installing Packages
# This step should be done in your terminal/command line interface.
# Command to create a virtual environment: python -m venv myenv
# Command to activate the virtual environment:
# On Windows: myenv\Scripts\activate
# On macOS/Linux: source myenv/bin/activate
# Command to install the requests package: pip install requests

import requests

# Task 2: Fetch Data from a Space API
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    return planets

def display_planet_info(planets):
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'N/A')
            mass = planet.get('mass', {}).get('massValue', 'N/A')
            orbit_period = planet.get('sideralOrbit', 'N/A')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda p: p.get('mass', {}).get('massValue', 0) if p['isPlanet'] else 0)
    return heaviest_planet

planets_data = fetch_planet_data()
display_planet_info(planets_data)

heaviest_planet = find_heaviest_planet(planets_data)
heaviest_planet_name = heaviest_planet.get('englishName', 'N/A')
heaviest_planet_mass = heaviest_planet.get('mass', {}).get('massValue', 'N/A')
print(f"The heaviest planet is {heaviest_planet_name} with a mass of {heaviest_planet_mass} x 10^24 kg")
