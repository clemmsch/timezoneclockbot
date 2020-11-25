import discord
from discord.ext import commands

import json

jsonFile = open('config.json')
data = jsonFile.read()

obj= json.loads(data)

client = commands.Bot(command_prefix = obj['prefix'])

@client.event
async def on_ready():
    print('Bot is ready, my prefix is: ')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client
# I AM ALIVE
client.run(obj['token'])