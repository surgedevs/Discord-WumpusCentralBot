## Author: @DzikStar
## Contributors: @DzikStar
##
## Description:
## This is main.py while which we will be using for running this bot.

import discord # pip install py-cord - not discordpy
import json

## Loading all configuration files which will be used by our client and bot
with open('config/userConfig.json') as userConfigFile:
    userConfig = json.load(userConfigFile)

with open('config/clientConfig.json') as clientConfigFile:
    clientConfig = json.load(clientConfigFile)

## Def of all main and important variables which will be used later in our code
discordAuthToken = str(userConfig['discordAuth'])
channelSupportChanges = str(clientConfig['secondsBetweenContentNextVerify'])
channelDatamining = str(clientConfig['secondsBetweenContentNextVerify'])
verifyCooldown = int(clientConfig['secondsBetweenContentNextVerify'])

## Idk what is that thing doing but okay :troll:
bot = discord.Bot()

## Place for slash commands

## Place for Bot tasks

# goofy ooh ahhh bot startup
bot.run(discordAuthToken)