import discord as d
from discord.ext import commands
import random
import os
from cogs import weather
import json
import requests
import cryptocompare


bot = commands.Bot(command_prefix = '$')
bot.remove_command('help')

@bot.event
async def on_ready(): 
    print('Logging in as {0.user}'.format(bot)) 
    await bot.change_presence(activity=d.Activity(type=d.ActivityType.watching, name="Darling!"))

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
thank_msg = ['thanks', 'thank', 'ty', 'grateful']
thanks_reply = ['you are welcome!', "don't mention it!", 'anytime!', 'I am glad i can help']

m_id = 720345337570787348

@bot.command(name="Hello",aliases=greetings)
async def Hello(ctx):
    if ctx.author.id == m_id :
        await ctx.send(random.choice(greetings)+" darling !")
        await ctx.send(":heart:")
    else:
        await ctx.send("Sorry ! I only talk to darling.")

@bot.command(name="Bye",aliases=['bye', 'cya','brb', 'gotta go', 'see', 'later'])
async def Bye(ctx):
    if ctx.author.id == m_id :
        await ctx.send(random.choice(bye_reply)+" darling !")
        await ctx.send(":heart:")
    else:
        await ctx.send("Sorry ! I only talk to darling.")

@bot.command(name="Thanks",aliases=thanks_msg)
async def Thanks(ctx):
    if ctx.author.id == m_id :
        await ctx.send(random.choice(thanks_reply)+" darling !")
        await ctx.send(":heart:")
    else:
        await ctx.send("Sorry ! I only talk to darling.")
 
@bot.command(name="Currency",aliases=currencies)
async def Currency(ctx):
    if ctx.author.id == m_id :
        btc_price = cryptocompare.get_price('BTC', curr= 'USD', full = False)['BTC']['USD']
    	   await ctx.send(f"1 BTC = {btc_price} USD")
    	   eth_price = cryptocompare.get_price('ETH', curr= 'USD', full = False)['ETH']['USD']
    	   await ctx.send(f"1 ETH = {eth_price} USD")
    	   ltc_price = cryptocompare.get_price('LTC', curr= 'USD', full = False)['LTC']['USD']
    	   await ctx.send(f"1 Litecoin = {ltc_price} USD")
    	   await ctx.send(":heart:")
        
    else:
        await ctx.send("Sorry ! I only talk to darling.")

@bot.command(name="Weather",aliases=["weather"])
async def Weather(ctx,city_name):
    if ctx.author.id == m_id :
        .lower():
        weather_info = weather(city_name)
        await ctx.send("Weather forensics for {} :\nTemperature :{} C\nPression : {} Pha\nHumidity : {} % ".format(city_name.capitalize(),weather_info[0],weather_info[1],weather_info[2]))
        await ctx.send(":heart:")
    else:
        await ctx.send("Sorry ! I only talk to darling.")

@bot.command(name="Ping",aliases=["ping"])
async def Ping(ctx):
    if ctx.author.id == m_id :
        await ctx.send(f"Sorry darling for keeping waiting for {bot.latency} ")
        await ctx.send(":heart:")
    else:
        await ctx.send("Sorry ! I only talk to darling.")
 
@bot.command(name="Question",aliases=["how","How","sup","Sup","Warup","warup","What's","what's","whats","Whats"])
async def Question(ctx):
    if ctx.author.id == m_id :
        await ctx.send(random.choice(a))
        await ctx.send(":heart:")
    else:
        await ctx.send("Sorry ! I only talk to darling.")
 
@bot.command(name="Love",aliases=["love","luv","Luv"])
async def Love(ctx):
    if ctx.author.id == m_id :
        await ctx.send(random.choice(love_response)+" darling !")
        await ctx.send(":heart:")
    else:
        await ctx.send("Sorry ! I only talk to darling.")
 
@bot.command(name="i",aliases=["I"])
async def i(ctx,mode,*args):
    if ctx.author.id == m_id :
    	   love_words = ["love", "loves", "Love", "Loves"]
    	   feels_words = ["feel", "Feel", "feels", "Feels"]
    	   if mode in love_words :
    	       await ctx.send(random.choice(love_response))
    	       await ctx.send(":heart:")
    	   elif mode in feels_words :
    	       await ctx.send(random.choice(sadness_response))
    	       await ctx.send(":heart:")
        else:
            pass
    else:
        await ctx.send("Sorry ! I only talk to darling.") 

@bot.command(name="Sadness",aliases=sadness_words)
async def Sadness(ctx):
    if ctx.author.id == m_id :
        await ctx.send(random.choice(sadness_response))
        await ctx.send(":heart:")
    else:
        await ctx.send("Sorry ! I only talk to darling.")

bot.event
    async def  on_command_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You can't do that ;-;")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter all the required arguments \ncalc [currentLvl] [targetLvl] [current%]* [target%]* ")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found, Please mention a valid user!")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I don't have the permissions to do that!")
        else:
            await ctx.send("Famma problem bb!")

bot.run(os.getenv("token"))











