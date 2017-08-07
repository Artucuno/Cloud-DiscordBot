# -*- coding: utf-8 -*-
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
    since = datetime.datetime(2017, 8, 1, 0, 0)
    days_since = (datetime.datetime.utcnow() - since).days
    em = discord.Embed(color=discord.Colour.red())
    em.add_field(name='Info', value=("\a"))
    em.add_field(name='Bot Owner', value=(list(config.OWNER)))
    em.add_field(name='Version', value=(discord.__version__))
    em.add_field(name='Description', value=("Cloud a multifunctunal discord bot by <@321193377951645699>!"))
    em.set_footer(text='Running bots Since {} days'.format(days_since))
    await c.say(embed=em)

@c.command()
async def say(*, msg=""):
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

@c.command(pass_context=True)
async def contact(ctx, *, msg):
    """I need help!"""
    author = ctx.message.author
    server = ctx.message.server
    inv = await c.create_invite(server)
    channel = c.get_channel("{}".format(config.CONTACTID))
    em = discord.Embed(color=discord.Colour.red())
    em.set_author(name="Contact by {}".format(author))
    em.add_field(name='Sent by', value=(author.mention))
    em.add_field(name='Server', value=(server))
    em.add_field(name='Message', value=(msg))
    em.add_field(name='Server Invite', value=(inv))
    em.set_thumbnail(url=server.icon_url)
    await c.send_message(channel, embed=em)
    em = discord.Embed(color=discord.Colour.red())
    em.add_field(name='Sent', value=("{} Help was sent please be patient! :thumbsup: ".format(author.mention)))
    em.set_footer(text="{} Will Look at your contact!".format(config.OWNER))        
    await c.say(embed=em)
@c.command(pass_context=True)
async def stats(ctx):
    """info about me!"""
    import time
    import psutil
    t1 = time.perf_counter()
    await c.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    cpu_p = psutil.cpu_percent(interval=None, percpu=True)
    cpu_usage = sum(cpu_p) / len(cpu_p)
    mem_usage = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
    users = str(len(set(c.get_all_members())))
    channels = len([c for c in c.get_all_channels()])
    text_channels = 0
    voice_channels = 0
    for channel in c.get_all_channels():
        if channel.type == discord.ChannelType.text:
            text_channels += 1
        elif channel.type == discord.ChannelType.voice:
            voice_channels += 1
    cols = [0x000000, 0x60ff07, 0x1107ff, 0x07ffd7]
    em = discord.Embed(color=random.choice(cols))
    avatar = c.user.avatar_url if c.user.avatar else c.user.default_avatar_url
    em.set_author(name='{} Stats!'.format("My", avatar))
    em.add_field(name='\a', value=("\n"
                                   "➠ Discord Ping **{}ms** :timer: \n\n"
                                   "➠ Memory Usage **{}** :computer: \n\n"
                                   "➠ CPU Usage    **{}%** :capital_abcd: \n\n"
                                   "➠ Servers      **{}** :globe_with_meridians: \n\n"
                                   "➠ Users        **{}** :man: \n\n"
                                   "➠ Channels     **{}** :hash: \n\n"
                                   "➠ Text Channels **{}** :hash: \n\n"
                                   "➠ Voice Channels **{}** :speaker: \n\n"
                                   "➠ Cogs         **{}** :exclamation: \n\n"
                                   "➠ API Version  **{}** :japanese_ogre: \n\n".format(str(round((t2-t1)*1000)), mem_usage, cpu_usage, len(c.servers), users, channels, text_channels, voice_channels, len(c.commands), discord.__version__)))
    await c.say(embed=em)
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
    print("{}\n"
          "\n"
          "Stats:\n"
          "Servers : {}\n"
          "Users   : {}\n"
          "Channels: {}\n".format(c.user.name, servers, users, channels))
    print("Need help? Join our Support server! https://discord.gg/h3AdAFd\n"
          "\n"
          "URL : https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0".format(c.user.id))
    print("\n"
          "Your bot is now online!")


run = run()
print(run)
