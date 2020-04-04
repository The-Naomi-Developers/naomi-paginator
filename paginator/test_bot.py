import discord
from discord.ext import commands

from paginator import Paginator


bot = commands.Bot(command_prefix='!')
token = 'token'

@bot.event
async def on_ready():
  print('im ready')


@bot.command()
async def paginate(ctx):
  """ Paginator test command """
  p = Paginator(ctx)

  embeds = ( discord.Embed(color=0xff0000, title='Embed #1', description='Test starts here'),
             discord.Embed(color=0x00ff00, title='Embed #2', description='Second embed...'),
             discord.Embed(color=0x0000ff, title='Embed #3', description='Last embed') )

  for x in embeds:
    p.add_page(x)

  await p.call_controller()


bot.run(token)
