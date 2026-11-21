import requests
# Location plaza mayor madrid
latitude = 40.4154
longuitde = -3.7074
# location for las rozas
latitude = 40.49176
longuitde = -3.873961
# URL (open-meteo API)
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longuitde}"
    "&current_weather=true"
)

#print(f"\n{url}\n")

#execute request
response = requests.get(url=url)


if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]
    print(f"\nTemperature: {weather["temperature"]}\n")
else:
    print(f"\nError al obtener los datos meteorologicos: {response.status_code}\n")




# Coordenadas para Plaza Mayor, Madrid
latitude = 40.4154
longitude = -3.7074

# Coordenadas para Las Rozas
# latitude = 40.49176
# longitude = -3.873961

# URL (Open-Meteo API)
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    "&current_weather=true"
)

# Ejecutar la solicitud
response = requests.get(url=url)

# Manejo de respuestas
if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]
    print(f"\nTemperature: {weather['temperature']}°C\n")
elif response.status_code == 400:
    print(f"\nError 400: Bad Request\n{url}\n")
elif response.status_code == 404:
    print("\nError 404: Not Found\n")
elif response.status_code == 500:
    print("\nError 500: Internal Server Error\n")
else:
    print(f"\nError desconocido: {response.status_code}\n")