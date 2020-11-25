import discord
from discord.ext import commands

import json

config = open("config.json")
jsondata = config.read()

obj = json.loads(jsondata)



client = commands.Bot(command_prefix = obj['prefix'])

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! ({round(client.latency * 1000)}ms)')



@client.command()
async def deleteClock(ctx, channel: discord.VoiceChannel):
    mbed = discord.Embed(
        title = 'Success',
        description = f'Clock: {channel} has been deleted'
    )
    if ctx.author.guild_permissions.manage_channels:
        await ctx.send(embed=mbed)
        await channel.delete()
    else:
        ctx.send('You do not have the permission to delete a clock!')





@client.command()
async def createClock(ctx, channelName, timezone):
    guild = ctx.guild

    mbed = discord.Embed(
        title = 'Success',
        description = "{} has been successfully created.".format(channelName)
    )
    if ctx.author.guild_permissions.manage_channels:
        name = f'{channelName} [{timezone}]'
        await guild.create_voice_channel(name='{}'.format(name))
        await ctx.send(embed=mbed)
    else:
        await ctx.send('You do not have the permissions to do this')






#######I AM ALIVE##########
client.run(obj['token'])


