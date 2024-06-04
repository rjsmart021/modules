import requests


def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    max_mass = float('-inf')
    heaviest_planet_name = ""
    min_mass = float('inf')
    lightest_planet_name = ""

    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']*(10**planet['mass']['massExponent'])
            orbit_period = planet["sideralOrbit"]
            print(f"Planet: {name}, Mass: {mass}, Orbit Period:\
            {orbit_period} days")

            if mass > max_mass:
                max_mass = mass
                heaviest_planet_name = name
            if mass < min_mass:
                min_mass = mass
                lightest_planet_name = name

    print(f"{heaviest_planet_name} is the heaviest planet in solar system with mass: {max_mass}")
    print(f"{lightest_planet_name} is the lightest planet in solar system with mass: {min_mass}")


fetch_planet_data()
