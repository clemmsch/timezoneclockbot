import discord
from discord.ext import commands
from discord.utils import find

import datetime
from datetime import datetime as dt
from time import gmtime, strftime
import time
import sched, time #The scheduler

import json

config = open("config.json")
jsondata = config.read()

obj = json.loads(jsondata)








#Time Setup

availableTimezones = ["CEST", "EET", "MST", "BST", "UTC"]
cestNow = False
eetNow = False
mstNow = False
bstNow = False
utcNow = False

client = commands.Bot(command_prefix = obj['prefix'])

@client.event
async def on_ready():
    print('Bot is ready.')

#The time-thing
s = sched.scheduler(time.time, time.sleep)

def timezoneHandler(): 
    print("Doing stuff...")
    # do your stuff
    s.enter(60, 1, timezoneHandler)
    s.run()

def calculateTimes():
    utcNow = dt.utcnow()

#Discord Commands
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! ({round(client.latency * 1000)}ms)')



@client.command()
async def deleteClock(ctx, channel: discord.VoiceChannel):
    mbed = discord.Embed(
        title = 'Success',
        description = f'Clock: {channel} has been deleted'
    #    color = 12117773
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
        description = "{} has been successfully created.".format(channelName),
   #     color = 12117773
    )
    if ctx.author.guild_permissions.manage_channels:
        name = f'{channelName} [{timezone}]'

        switch (timezone) {
            case "UTC":
                await ctx.send("YOO UTC")
        }
        
        await guild.create_voice_channel(name='{}'.format(name))
        await ctx.send(embed=mbed)




    else:  
        await ctx.send('You do not have the permissions to do this')

@client.command()
async def timezones(ctx):
    mbed = discord.Embed(
        title = 'All Timezones',
        description = "Central European Standart Time, CEST (UTC+2) \n \n Eastern European Time, EET (UTC+2) \n \n Mountain Standard Time, MST (UTC-7) \n \n Brazilian Standart Time, BST (UTC-3)",
      #  color = 12117773
        )
    await ctx.send(embed=mbed)

# Timezone Functions




#######I AM ALIVE##########
client.run(obj['token'])


