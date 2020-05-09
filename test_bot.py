# -*- coding: utf-8 -*-

"""MIT License

Copyright (c) 2020 Naomi-Bot-Open-Source

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
from discord.ext import commands

from naomi_paginator import Paginator


bot = commands.Bot(command_prefix='!')
token = 'your-bot-token'

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
