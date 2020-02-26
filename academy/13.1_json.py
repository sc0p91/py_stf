#!/home/swan/python/venvs/experiment/bin/python3.7

import requests, sys, json, pytemperature
from argparse import ArgumentParser
from math import floor

api_key='21968e47279f8f00941fd808131c7b5d'

parser = ArgumentParser(description="Get Weather for a set place")
parser.add_argument('zip', help="Zip code")
parser.add_argument('--country', default="ch", help="The Country - default ch")

args = parser.parse_args()

url=f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res = requests.get(url)

if res.status_code != 200:
    print(f"Error! {res.status_code}")
    sys.exit(1)

main = res.json()['main']

for content in res.json()['weather']:
    print(f"{res.json()['name']}'s current Weather: {content['main']} - {content['description']}")

print(f"Temp: {floor(pytemperature.k2c(main['temp']))}°C, Min/Max: \
{floor(pytemperature.k2c(main['temp_min']))}°C/{floor(pytemperature.k2c(main['temp_max']))}°C \
Humidity: {main['humidity']}%")

