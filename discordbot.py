import discord
import os
import time
import random
from discord.ext import commands
import asyncio
import json
import http.client
import urllib.request


bot = commands.Bot(command_prefix="hh ")


appends = [
    "idiotic",
    "dumb",
    "stupid",
    "dum dum",
    "gae",
    "useless",
    "idot"
]
@bot.event
async def on_ready():
    print("Ready")
@bot.command()
async def sayit(ctx, name):
    message = name
    await ctx.channel.send(message + " is " + appends[random.randint(0, len(appends))])
@bot.command()
async def hello(ctx):
    await ctx.channel.send("Huy Hoang is dumb")
@bot.command()
async def dadjoke(ctx):
    conn = http.client.HTTPSConnection("dad-jokes.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
        'x-rapidapi-key': "a2dce5d962mshf5eb203579dfd40p1bcf50jsn3398b84a9180"
    }

    conn.request("GET", "/random/joke", headers=headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode('utf-8'))
    await ctx.channel.send("Dad joked: " + data['body'][0]['setup'] + " | " + data['body'][0]['punchline'])
@bot.command()
async def rule34(ctx, tag):
    message = tag
    if message == "random":
                url = "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=*%20-furry_*%20-furry%20-pets%20-animals%20-pet%20-animal"
                with urllib.request.urlopen(url) as r34:
                    data = json.loads(r34.read().decode())
                    data_return = data[random.randint(0, len(data))]['sample_url']
                await ctx.channel.send(data_return)
    else:
            url = "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=" + message + "%20-furry_*%20-furry%20-pets%20-animals%20-pet%20-animal"
            
            try:
                with urllib.request.urlopen(url) as r34:
                    data = json.loads(r34.read().decode())
                    data_return = data[random.randint(0, len(data))]['sample_url']
                await ctx.channel.send(data_return)
            except json.JSONDecodeError:
                await ctx.channel.send("Invalid keywords, please try again")
            except json.IndexError:
                await ctx.channel.send("Can't find anything with the given keyword") 
@bot.command()
async def getmeme(ctx):
    with urllib.request.urlopen("https://meme-api.herokuapp.com/gimme") as meme_url:
        data = json.loads(meme_url.read().decode())
        data_return = data['preview'][3]
    await ctx.channel.send(data_return)
@bot.command()
async def howgay(ctx, name):
    gayness = random.randint(0, 101)
    await ctx.channel.send(name + " is " + str(gayness) + "% gay :gay_pride_flag:")
@bot.command()
async def howsimp(ctx, name):
    simpness = random.randint(0, 101)
    await ctx.channel.send(name + " is " + str(simpness) + "% simp")
@bot.command()
async def space(ctx):
    with urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=BWZFUWV4cds8JjCtYFxrfOMJRJRXDKElUHXhCgzC") as nasa:
        data = json.loads(nasa.read().decode())
        nasa_image = data['url']
        explain = data['explanation']
    await ctx.channel.send(nasa_image)
    await ctx.channel.send(explain)
@bot.command()
async def gethelp(ctx):
    await ctx.channel.send("""
Hello! I am a bot based on my retarded friend Nguyen Huy Hoang
- Some commands you can use (prefix: hh)
    + hh space - Generates the Space Picture of the Day from NASA.
    + hh dadjoke - Generates a Dad Joke, make your day!
    + hh howgay @username - Measures your gayness.
    + hh howsimp @username - Measures your simpness.
    + hh sayit @username - Attach the name with wonderful words.
    + hh getmeme - Get a meme.
    + hh rule34 (tags) - You know what this does. If have multiple tags, add a %20 as a space
And thats it, enjoy. 
Huy Hoang, you are still retarded.
    """)
bot.run("OTUzODM3MzA4MzAwMzc4MTgy.YjKYNw.C29Xfp5S4gQT3h-WFkBofp5mGAE")