import os
import discord
from discord.ext import commands

import commandsFile

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 234708273851400192 # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def name(ctx):
    await ctx.send(commandsFile.name(ctx))

@bot.command()
async def count(ctx):
    await ctx.send(commandsFile.count(ctx, bot))

@bot.command()
async def admin(ctx, user):
    await ctx.send(commandsFile.put_admin(ctx, user))

@bot.command()
async def xkcd(ctx):
    await ctx.send(commandsFile.put_commic(ctx))

@bot.command()
async def poll(ctx, *args):
    await commandsFile.create_poll(ctx, args)

token = "ODkyODIyOTE0NTQwMzk2NjQ0.YVSgIg.9WQQ1Aefi6dRzyDZAp01axW5OFo"
bot.run(token)  # Starts the bot

