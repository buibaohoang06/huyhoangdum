from discord.ext import commands
import json
import urllib.request
import random
import requests
import asyncio
import discord
from pytube import YouTube
import os
import ffmpeg

bot = commands.Bot(command_prefix="#")

@bot.event
async def on_ready():
    print("Ready")
@bot.command()
async def test(ctx):
    await ctx.channel.send("I'm still here!")
@bot.command()
async def apod(ctx):
    r = requests.get("https://api.nasa.gov/planetary/apod?api_key=BWZFUWV4cds8JjCtYFxrfOMJRJRXDKElUHXhCgzC").status_code
    if r == 200:
        with urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=BWZFUWV4cds8JjCtYFxrfOMJRJRXDKElUHXhCgzC") as nasa:
            data = json.loads(nasa.read().decode())
            image = data['url']
        await ctx.channel.send(image)
    else:
         await ctx.channel.send(f"Error occured! Status code: {r} | Looks like you got something wrong or the API is down. Try again.")
@bot.command()
async def mars(ctx, date):
    r = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key=BWZFUWV4cds8JjCtYFxrfOMJRJRXDKElUHXhCgzC").status_code
    if r == 200:
        with urllib.request.urlopen(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key=BWZFUWV4cds8JjCtYFxrfOMJRJRXDKElUHXhCgzC") as mars:
            data = json.loads(mars.read().decode())
            image = data['photos'][random.randint(0, len(data['photos']))]['img_src']
        await ctx.channel.send(image)
    else:
        await ctx.channel.send(f"Error occured! Status code: {r} | Looks like you got something wrong or the API is down. Try again.")
@bot.command()
async def earth(ctx):
    from datetime import date
    await ctx.channel.send("Printing the latest image of Earth")
    today = date.today()
    with urllib.request.urlopen("https://api.nasa.gov/EPIC/api/natural?api_key=BWZFUWV4cds8JjCtYFxrfOMJRJRXDKElUHXhCgzC") as getName:
        data = json.loads(getName.read().decode())
        name = data[0]['image']
    r = requests.get(f"https://api.nasa.gov/EPIC/archive/natural/{today.year}/{today.month}/{today.day}/png/{name}.png?api_key=BWZFUWV4cds8JjCtYFxrfOMJRJRXDKElUHXhCgzC").status_code
    if r == 200:
        await ctx.channel.send(f"https://api.nasa.gov/EPIC/archive/natural/{today.year}/{today.month}/{today.day}/png/{name}.png?api_key=BWZFUWV4cds8JjCtYFxrfOMJRJRXDKElUHXhCgzC")
    else:
        await ctx.channel.send(f"Error occured! Status code: {r} | Looks like you got something wrong or the API is down. Try again.")
@bot.command()
async def play(ctx, addr):
    import time
    audio = YouTube(addr).streams.filter(only_audio=True).first()
    out_file = audio.download(output_path='.')
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    member = discord.Member
    channel = member.voice.channel
    if channel:
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=f"{audio.name}.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            time.sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send("Stopped!")

bot.run("OTU0MDAzMjU3NzkyMDA0MTA3.YjMyxQ.nWH-TAWDAT7KiKHrVuTiAt2WzIA")