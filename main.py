## Author: @DzikStar
## Contributors: @DzikStar
##
## Description:
## This is main.py while which we will be using for running this bot.

import discord ## `pip install py-cord` - not discordpy
import json
import os
import time
import asyncio
from utils import workerLogs
from lib import supportTask

config_path = os.path.join(os.path.dirname(__file__), 'config', 'userConfig.json')
with open(config_path) as userConfigFile:
    userConfig = json.load(userConfigFile)

config_path = os.path.join(os.path.dirname(__file__), 'config', 'clientConfig.json')
with open(config_path) as clientConfigFile:
    clientConfig = json.load(clientConfigFile)

bot = discord.Bot()

## Place for slash commands
@bot.slash_command(name = "testing", description = "super duper testing command")
async def testing(ctx):
    ## This command is replyign with a message to a user, nothing more. Using 
    await ctx.respond("Hey! We're actually testing some stuff with our bot. If you are interested in development of our bot then you can be interested :troll:")
    print(workerLogs.userUsedCommand(member=str(ctx.author.name), commandName=str('testing'), executeType=int(2)))

## Place for Bot tasks
async def supportTrackerTask():
    await bot.wait_until_ready()
    firstLaunch = bool(True)
    while True:
        if firstLaunch == True:
            ## Downloading two RSS files
            ## First file is older, it's from our database repository
            ## Seconds is a new file, it's RSS from big nutty GitLab repository
            supportTask.importAllFiles(GHPAtoken=userConfig['githubDatabasePAToken'])

        print(workerLogs.supportTracker(stage=1))

        ## Everything is done now so this task can now wait until next loop
        await asyncio.sleep(clientConfig['secondsBetweenRSSContentNextVerify'])

## Client Startup
bot.loop.create_task(supportTrackerTask()) ## Support Changes
bot.run(userConfig['discordAuth'])