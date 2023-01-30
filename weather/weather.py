import requests
from pprint import pprint

API_Key = "e83c18b5bbedc8218009da901368877e"

location = input("ENTER THE LOCATION FOR WEATHER INFO : ")

weather_url = f"http://api.openweathermap.org/data/1.5/weather?q={location}&appid={API_Key}"
# final_url = weather_url+ API_Key
weather_data = requests.get(weather_url).json()
pprint(weather_data)