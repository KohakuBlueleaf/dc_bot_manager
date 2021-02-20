import os,sys
from discord.ext import commands
from json import loads


config = loads(sys.argv[1])

bot = commands.Bot(command_prefix=config['prefix'], description=config['description'])
bot.load_extension(config['extension_path'])
bot.run(config['token'])
