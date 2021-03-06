import requests
import json
import PySimpleGUI as sg

def callWeatherApi(city):
    api_key = "736e90ffa8b745b5b82c3fee64e9a86e"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    return response.json()






layout = [
            [sg.Text(text="Write the city: "), sg.InputText(text_color="red")],
            [sg.Button(button_text="Search"),sg.Button(button_text="Exit")],
            [sg.Text(key="_CITY_", size=(20,1),text_color="Red",text="",auto_size_text=False)],
                [sg.Text(key="_MAIN_", text="", size=(50,1))],
                [sg.Text(key="_DESCRIPTION_", text="", size=(50,1))],
                [sg.Image(key="_IMAGE_")],
                [sg.Text(key="_TEMPERATURE_", text="", size=(50,1))]

          ]

window = sg.Window('Forecast Weather', layout, no_titlebar=True, grab_anywhere=True)


while True:
    event, values = window.read()
    if event == "Exit" or sg.WIN_CLOSED:
        break
    elif event == "Search":
        cityInfo = callWeatherApi(values[0])
        city = cityInfo['name']
        main = cityInfo['weather'][0]['main']
        description = cityInfo['weather'][0]['description']
        icon = cityInfo['weather'][0]['icon']
        print(icon)
        window["_CITY_"].update(city)
        window['_MAIN_'].update(main)
        window['_DESCRIPTION_'].update(description)
        window["_IMAGE_"].update(rf'C:\Users\Miguel\PycharmProjects\preparcial\Project\Icons\{icon}.png')


window.close()

example = \
{
    'coord': {'lon': -97.85, 'lat': 22.22},
     'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}],
     'base': 'stations',
     'main': {'temp': 301.15, 'feels_like': 303.91, 'temp_min': 301.15, 'temp_max': 301.15, 'pressure': 1012, 'humidity': 69},
     'visibility': 10000,
     'wind': {'speed': 2.6, 'deg': 70},
     'clouds': {'all': 40},
     'dt': 1605124248,
     'sys': {'type': 1, 'id': 7173, 'country': 'MX', 'sunrise': 1605098496, 'sunset': 1605138573},
     'timezone': -21600,
     'id': 3516355,
     'name': 'Tampico',
     'cod': 200
 }
