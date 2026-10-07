# Install a external module and use it to perform an action

import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m")

data = response.json()

print(data)