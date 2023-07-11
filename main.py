import requests

api_key = "5a51a8b293d17182442a082e27ead661"
city = input("Enter Your City: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?"

url_ok = base_url + "appid=" + api_key + "&units=metric" + "&q=" + city

response = requests.get(url_ok)

data = response.json()

if response.status_code != 404:
      clouds_state = data['weather'][0]['description']
      temperature = data['main']['temp']
      temperature_feel = data['main']['feels_like']
      temperature_min = data['main']['temp_min']
      temperature_max = data['main']['temp_max']
      pressure_state = data['main']['pressure']
      humidity_state = data['main']['humidity']
      wind_state = data['wind']['speed']
      wind_direction = data['wind']['deg']
      print(f"City: ", city.capitalize())
      print("Temperature: {} \nFeels Like: {} \nMin Temp: {} \nMax Temp: {} \nPressure: {} hPa \nHumidity: %{}"
            .format(temperature, temperature_feel, temperature_min, temperature_max, pressure_state, humidity_state))
      print("Wind State: {} m/s, {} deg.".format(wind_state, wind_direction))

else:
      print("Page Not Found 404")






