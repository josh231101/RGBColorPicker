import requests
import json

api_key = ""

base_url = "WEATHER API BASE URL"

city_name = input("City Name: ")

complete_url = base_url + "appid=" + api_key + "&q" + city_name

response = requests.get(complete_url)

x = response.json()

