# bot.py

import asyncio
import os
import discord
import youtube_dl
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
token = 'NjYzNjA4OTA3NjY2ODE3MDY0.XhLNyg.xLlJEgs-vEHbOSvqAaDWMXg_9y0'
guild = 'www.RickandMortyAdventureswww.com'

# client = discord.Client()
client = commands.Bot(command_prefix= '.')
players = {}

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == guild:
            break

    print(
        f'{client.user} is connected to Discord!'
    )


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete old file but it is being played")
        await ctx.send("ERROR: Music playing")
        return

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio")
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed file: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"{name} has finished playing"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    new_name = name.rsplit("-", 2)
    await ctx.send(f"Playing: {new_name}")
    print("playing\n")

@client.command()
async def r2(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete old file but it is being played")
        await ctx.send("ERROR: Music playing")
        return

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio")
        ydl.download(['https://www.youtube.com/watch?v=B6mh45mA_JY'])

    for file in os.listdir('./'):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed file: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"{name} has finished playing"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.70

    new_name = name.rsplit("-", 2)
    await ctx.send(f"Playing: {new_name}")
    print("playing\n")

    #await ctx.voice_client.disconnect()

@client.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

client.run(token)
