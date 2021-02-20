import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound


##修飾器
def event_with_error(func):
  async def function(*args,**kwargs):
    try:
      return (await func(*args, **kwargs))
    except:
      err = format_exc()
      log_error_event(err)
  function.__name__ = func.__name__
  return function


class test(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  @event_with_error
  async def on_ready(self):
    print('Logged in as')
    print(self.bot.user.name)
    print(self.bot.user.id)
    await self.bot.change_presence(status=discord.Status.online, activity=discord.Game("CoC七版"))
    print('------')

  @commands.Cog.listener()
  @event_with_error
  async def on_command_error(self,ctx, error):
    if isinstance(error, CommandNotFound):
      return
    try:
      raise error
    except Exception:
      err = format_exc()
      log_error_command(err)

  @commands.command()
  async def helloworld(self, ctx):
    await ctx.send('Hello Discord!')

def setup(bot):
  bot.add_cog(chimin(bot))