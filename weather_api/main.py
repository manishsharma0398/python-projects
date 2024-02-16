"""weather app"""

import requests
import json
import os
import platform

system_os = platform.system()
COMMAND = "wsay.exe" if "windows" in system_os.lower() else "say"

city = input("\nEnter name of city (city, state for accurate results): ")

url = f"https://api.weatherapi.com/v1/current.json?key=adc1433b3b724146954163224241302&q={city}"

r = requests.get(url, timeout=15)

weather_dict = json.loads(r.text)

temp = weather_dict["current"]["temp_c"]

os.system(f'{COMMAND} "The current weather in {city} is {temp} degree celsius"')
