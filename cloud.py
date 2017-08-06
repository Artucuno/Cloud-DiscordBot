import discord
from discord.ext.commands import Bot
from discord.ext import commands
import logging
import sys
import os
import config
import random
import datetime

# Cloud a discord bot made by Cloud#6618
# Need Support? join the Cloud Server! https://discord.gg/h3AdAFd

def clear_screen():
    IS_WINDOWS = os.name == "nt"
    IS_MAC = sys.platform == "darwin"
    INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
c = Bot(command_prefix=config.PREFIX) # Sets the client and sets the prefix

@c.command(pass_context=True)
async def info(ctx):
    """"""
    since = datetime.datetime(2017, 8, 6, 0, 0)
    days_since = (datetime.datetime.utcnow() - since).days
    em = discord.Embed(color=discord.Colour.red())
    em.add_field(name='Info', value=("\a"))
    em.add_field(name='Bot Owner', value=(list(config.OWNER)))
    em.add_field(name='Version', value=(discord.__version__))
    em.add_field(name='Description', value=("Cloud a multifunctunal discord bot by <@321193377951645699>!"))
    em.set_footer(text='Running bots Since {} days'.format(days_since))
    await c.say(embed=em)

@c.command()
async def say(msg=""):
    """hi"""
    if msg == "":
        await c.say("```\n"
                    "{}say <msg>\n"
                    "\n"
                    "'hi'```".format(config.PREFIX))
    try:
        await c.say(msg)
    except:
        pass


def run():
    c.run(config.TOKEN) # Starts to run your bot

@c.event
async def on_command(message, member):
    # Says when someone uses a command
    print("[Command] {}{}".format(config.PREFIX, message))
@c.event
async def on_ready():
    users = len(set(c.get_all_members()))
    servers = len(c.servers)
    channels = len([c for c in c.get_all_channels()])
    # when the bot is ready
    clear_screen()
    print("----------------\n"
          "Cloud-DiscordBot\n"
          "----------------\n")
    print("\n"
          "Stats:\n"
          "Servers : {}\n"
          "Users   : {}\n"
          "Channels: {}\n".format(servers, users, channels))
    print("\n"
          "URL : https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0".format(c.user.id))
    print("\n"
          "Your bot is now online!")


run = run()
print(run)
