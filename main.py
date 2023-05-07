##
## Author: @DzikStar
## Contributors: @DzikStar
##
## Description:
## This is main.py while which we will be using for running this bot.
##

import json
import requests
import discord

# Loading all configuration files which will be used by our client and bot
with open('userConfig.json') as userConfigFile:
    userConfig = json.load(userConfigFile)

with open('clientConfig.json') as clientConfigFile:
    clientConfig = json.load(clientConfigFile)

# Def of all main and important variables which will be used later in our code
discordAuthToken = userConfig['discordAuth']

# Idk what is that thing doing but okay :troll:
bot = discord.Bot()

@bot.slash_command()
async def hello(ctx, name: str = None):
    ## Example for documentation
    ## Every command should have docs before creation
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")

bot.run(discordAuthToken)