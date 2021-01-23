import discord
import os
import random
from keep_alive import keep_alive
import webbrowser
from bs4 import BeautifulSoup
import requests, json 
import cryptocompare

#################### functions #######################
def weather(city_name):
  forensics = []
  api_key = os.getenv("key")
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  response = requests.get(complete_url) 
  x = response.json() 
  if x["cod"] != "404": 
    y = x["main"] 
    current_temperature = y["temp"] - 273.15
    forensics.append(current_temperature)
    current_pressure = y["pressure"]
    forensics.append(current_pressure)
    current_humidity = y["humidity"]
    forensics.append(current_humidity)
    z = x["weather"] 
    weather_description = z[0]["description"] 
    return forensics
  else :
    forensics = ["None","None","None"]
    return forensics
  
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

######################################################

client = discord.Client()
##################### msgs ###########################
# love
love_msgs = ['i love you', 'love ya', 'luv ya', 'love', "luv u"]
love_response = ['love u 2 darling', 'love ya', 'love ya babe', 'love you more darling']
# greetings
greetings = ['hello', 'hi', 'hey', 'oi']
# sadness
sadness_words = ['sad', 'depressed', 'desperate', 'suicide']
sadness_response = ['cheer up, darling', 'dont be sad darling']
#how are you
q= ['how are you', 'how have you been',"what's up", 'warup', 'sup']
a= ['fine darling','Im fine darling i missed you','im doing fine bae']
# bye msgs
bye_msg = ['bye', 'cya','brb', 'gotta go', 'i have to go', 'see you later', 'later']
bye_reply = ['bye', 'cya', 'okay later', 'ok', 'take care','have fun', 'hf tc', 'tc']
#currencies 
currencies = ['usd','dollar','euro','bitcoin','litecoin','etherium','dinar','flous']
#thanks
thanks = ['thanks', 'thank', 'ty', 'grateful']
thanks_reply = ['you are welcome!', "don't mention it!", 'anytime!', 'I am glad i can help']

######################################################


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  try:
    if msg.startswith("$"):
      if str(message.author).lower() == 'ceiv#2485':
        #love
        if any(word in msg[1:].lower() for word in love_msgs):
          await message.channel.send(random.choice(love_response))
        #greetings
        if any(word in msg[1:].lower() for word in greetings):
          await message.channel.send(random.choice(greetings)+" darling")
        #sadness
        if any(word in msg[1:].lower() for word in sadness_words):
          await message.channel.send(random.choice(sadness_response))
        #how are you
        if any(word in msg[1:].lower() for word in q):
          await message.channel.send(random.choice(a))
        #bye
        if any(word in msg[1:].lower() for word in bye_msg):
          await message.channel.send(random.choice(bye_reply)+" darling")
        #thanks
        if any(word in msg[1:].lower() for word in thanks):
          await message.channel.send(random.choice(thanks_reply)+" darling")

        #weather 
        if "weather" in msg.lower():
          mylist = weather(msg[9:])
          await message.channel.send("Weather forensics for {} :\nTemperature :{} C\nPression : {} Pha\nHumidity : {} % ".format(msg[9:],mylist[0],mylist[1],mylist[2]))
        
        #bitcoin
        if any(word in msg[1:].lower() for word in currencies):
          btc_price = cryptocompare.get_price('BTC', curr= 'USD', full = False)['BTC']['USD']
          await message.channel.send(f"1 BTC = {btc_price} USD")
          eth_price = cryptocompare.get_price('ETH', curr= 'USD', full = False)['ETH']['USD']
          await message.channel.send(f"1 ETH = {eth_price} USD")
          ltc_price = cryptocompare.get_price('LTC', curr= 'USD', full = False)['LTC']['USD']
          await message.channel.send(f"1 Litecoin = {ltc_price} USD")

        await message.channel.send(":heart:")
      else :
        await message.channel.send("Sorry, I only talk to darling!")
  except :
    await message.channel.send("Famma problem bb!")
      
#keeping darling alive     
keep_alive()
client.run(os.getenv("token"))
