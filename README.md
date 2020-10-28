# Naomi Paginator
Simple paginator with reaction control, written in Python for `discord.py` bots.
Used in our bot (https://naomi.life)

[![CodeFactor](https://www.codefactor.io/repository/github/the-naomi-developers/naomi-paginator/badge)](https://www.codefactor.io/repository/github/the-naomi-developers/naomi-paginator) 
[![PyPI version](https://badge.fury.io/py/naomi-paginator.svg)](https://badge.fury.io/py/naomi-paginator) 

# Usage:
```py
import discord
from discord.ext import commands

from naomi_paginator import Paginator

bot = commands.Bot(command_prefix='!')

@bot.command()
async def paginate(ctx):
  """Paginator test command."""
  p = Paginator(ctx)

  embeds = (discord.Embed(color=0xff0000, title='Embed #1', description='Test starts here'),
            discord.Embed(color=0x00ff00, title='Embed #2', description='Second embed...'),
            discord.Embed(color=0x0000ff, title='Embed #3', description='Last embed'))

  for x in embeds:
    p.add_page(x)

  await p.call_controller()

bot.run('token')
```

# Installing
```sh
# From source:
$ pip3 install git+https://github.com/The-Naomi-Developers/naomi-paginator

# From PyPI:
$ pip3 install naomi-paginator
```

# License
```
MIT License

Copyright (c) 2020 The-Naomi-Developers

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
```
