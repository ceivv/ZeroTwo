import json
import requests
import cryptocompare


def weather(city_name):
  forensics = []
  api_key = os.getenv("key")
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  response = requests.get(complete_url) 
  weather_data = response.json() 
  if weather_data["cod"] != "404": 
    weather_main = weather_data["main"] 
    current_temperature = weather_main["temp"] - 273.15
    forensics.append(current_temperature)
    current_pressure = weather_main["pressure"]
    forensics.append(current_pressure)
    current_humidity = weather_main["humidity"]
    forensics.append(current_humidity)
    weather_desc = weather_data["weather"] 
    weather_description = weather_desc[0]["description"] 
    return forensics
  else :
    forensics = ["None","None","None"]
    return forensics


######################

  
"""def money():
  btc_price = cryptocompare.get_price('BTC', curr= 'USD', full = False)['BTC']['USD']
  print(f"1 BTC = {btc_price} USD")
  eth_price = cryptocompare.get_price('ETH', curr= 'USD', full = False)['ETH']['USD']
  print(f"1 ETH = {eth_price} USD")
  ltc_price = cryptocompare.get_price('LTC', curr= 'USD', full = False)['LTC']['USD']
  print(f"1 Litecoin = {ltc_price} USD")
  tnd_price = cryptocompare.get_price('TND', curr= 'USD', full = False)['TND']['USD']
  print(f"1 TND = {tnd_price} USD")
  tnd_to_euro = cryptocompare.get_price('TND', curr= 'EUR', full = False)['TND']['EUR']
  print(f"1 TND = {tnd_tnd_to_euro} EUR")"""