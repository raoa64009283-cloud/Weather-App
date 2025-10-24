#weather console project
import requests
from colorama import Fore, Style

def getWeather(location):
    try:
        api = requests.get(f"https://goweather.xyz/weather/{location.capitalize()}")
        data = api.json()
        print(Fore.RED + "City: " + Style.RESET_ALL + f"{location.capitalize()}\n"+
              Fore.RED + "Temperature: " + Style.RESET_ALL + f"{data["temperature"]}\n"+
              Fore.RED + "Wind: " + Style.RESET_ALL + f"{data["wind"]}\n"+
              Fore.RED + "Condition: " + Style.RESET_ALL + f"{data["description"]}\n")
    except requests.exceptions.RequestException:
        print(Fore.RED + "404: City not found!" + Style.RESET_ALL)

repeat = True

while repeat == True:
    answer = input("Select a city to check it's weather: ")
    if answer:
        getWeather(answer)
    else:
        repeat = False
