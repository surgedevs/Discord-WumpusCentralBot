## Author: @DzikStar
## Contributors: @DzikStar
##
## Description:
## This is main.py while which we will be using for running this bot.

import discord # pip install py-cord - not discordpy
import json
import os

## Loading all configuration files which will be used by our client and bot
config_path = os.path.join(os.path.dirname(__file__), 'config', 'userConfig.json')
with open(config_path) as userConfigFile:
    userConfig = json.load(userConfigFile)

config_path = os.path.join(os.path.dirname(__file__), 'config', 'clientConfig.json')
with open(config_path) as clientConfigFile:
    clientConfig = json.load(clientConfigFile)

## Def of all main and important variables which will be used later in our code
discordAuthToken = str(userConfig['discordAuth'])
channelSupportChanges = str(clientConfig['secondsBetweenContentNextVerify'])
channelDatamining = str(clientConfig['secondsBetweenContentNextVerify'])
SupportChangesGitLabRSS = str('https://gitlab.com/derpystuff/discord-support/-/commits/main?format=atom')
AssetsChangesGitLabRSS = str('https://gitlab.com/derpystuff/discord-asset-datamining/-/commits/master?format=atom')

verifyCooldown = int(clientConfig['secondsBetweenContentNextVerify'])

## Idk what is that thing doing but okay :troll:
bot = discord.Bot()

## Place for slash commands

## Place for Bot tasks

# goofy ooh ahhh bot startup
bot.run(discordAuthToken)