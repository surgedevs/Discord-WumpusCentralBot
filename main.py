"""
:author @DzikStar
:contributors @DzikStar

This is main.py while which we will be using for running this bot.
"""

import discord
import json
import os
import asyncio

import enums.Stage
from utils import worker_logs
from lib import support_task
from discord.ext import commands, tasks

config_path = os.path.join(os.path.dirname(__file__), 'config', 'userConfig.json')
with open(config_path) as userConfigFile:
    userConfig = json.load(userConfigFile)

config_path = os.path.join(os.path.dirname(__file__), 'config', 'clientConfig.json')
with open(config_path) as clientConfigFile:
    clientConfig = json.load(clientConfigFile)

bot = discord.Bot()


@bot.slash_command(name="testing", description="super duper testing command")
async def testing(ctx: commands.Context) -> None:
    """
    Replies with a predetermined message.

    :param ctx: discord.ext.commands.Context
    :return: None
    """

    await ctx.reply(
        "Hey! We're actually testing some stuff with our bot. "
        + "If you are interested in development of our bot then you can be interested :troll:"
    )

    print(
        worker_logs.user_used_command(
            member=ctx.author.name,
            command_name='testing',
            execute_type=2
        )
    )


@tasks.loop()
async def support_tracker_task() -> None:
    """
    Function for various Bot tasks

    :return: None
    """

    print(worker_logs.support_tracker(enums.Stage.Stage.AFTER_STARTUP))

    # wait until next loop
    await asyncio.sleep(clientConfig['secondsBetweenRSSContentNextVerify'])


def support_tracker_first_launch() -> None:
    """
    first launch of the support_tracker

    :return: None
    """

    # Downloads RSS files from our db repo (older) and from BigNutty's repo (newer)
    support_task.import_all_files(ghp_atoken=userConfig['githubDatabasePAToken'])


# Startup
support_tracker_first_launch()
support_tracker_task.start()
bot.run(userConfig['discordAuth'])
