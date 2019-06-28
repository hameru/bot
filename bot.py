import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Final Fantasy XIV: Shadowbringers'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content.startswith('is shb out'):
        randomlist = ["YES! FUCK OFF!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('is shadowbringers out'):
        randomlist = ["YES!"]
        await client.send_message(message.channel,(random.choice(randomlist)))

    if message.content.startswith('is Shadowbringers out'):
        randomlist = ["YES!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('is Shb out'):
        randomlist = ["YES!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == 'how long until shb':
        await client.send_message(message.channel,'GO PLAY!')
    if message.content.startswith('Is shb out'):
        randomlist = ["YES!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('Is shadowbringers out'):
        randomlist = ["YES!"]
        await client.send_message(message.channel,(random.choice(randomlist)))

    if message.content.startswith('Is Shadowbringers out'):
        randomlist = ["YES!",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('Is Shb out'):
        randomlist = ["YES!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == 'How long until shb':
        await client.send_message(message.channel,'GO PLAY!')
        
client.run('NTQzNDExNzk2MDU3MzkxMTM0.Dz-n4A.2j1KT-Aaz4Fw7iTfWXLKHJplQWQ')
