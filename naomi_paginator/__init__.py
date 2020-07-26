# -*- coding: utf-8 -*-

"""
MIT License

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

from discord import Embed, errors.NotFound
from discord.ext.commands import Context
from asyncio import TimeoutError
from typing import Union


class Paginator:
  def __init__(self, ctx: Context, reactions: Union[tuple, list] = None, timeout: int = 120):
    """ Init paginator.

    Args:
    -----
    * ctx: `commands.Context`: current context

    * reactions: `tuple` or `list`: custom emoji list (default: None)
      tip: [left_arrow, destroy_embed, right_arrow] - only 3 emojis

    * timeout: `int`: timeout in seconds (default: 120)
    """
    self.reactions = reactions or ('⬅', '⏹', '➡')
    self.pages = []
    self.current = 0
    self.ctx = ctx
    self.timeout = timeout


  async def _close_session(self):
    try:
      await self.controller.delete()
    except errors.NotFound:
      pass
    
    del self.pages
    del self.reactions
    del self.current
    del self.ctx


  def add_page(self, embed: Embed):
    """ Add new page to paginator.
    
    Args:
    -----
    * embed: discord.Embed
    """
    self.pages.append(embed)


  async def call_controller(self, start_page: int = 0):
    """ Call controller.
    
    Args:
    -----
    * start_page: int: start paginator from given page (default: 0 - first added page)
    """
    if start_page > len(self.pages) - 1:
      raise IndexError(f'Currently added {len(self.pages)} pages,\
        but you tried to call controller with start_page = {start_page}')

    self.controller = await self.ctx.send(embed=self.pages[start_page])

    for emoji in self.reactions:
      await self.controller.add_reaction(emoji)

    while True:
      try:
        response = await self.ctx.bot.wait_for('reaction_add', timeout=self.timeout,
          check=lambda r, u: u.id == self.ctx.author.id and r.emoji in self.reactions\
            and r.message.id == self.controller.id)
      except TimeoutError:
        break
      
      try:
        await self.controller.remove_reaction(response[0], response[1])
      except:
        pass
      
      if response[0].emoji == self.reactions[0]:
        self.current = self.current - 1 if self.current > 0 else len(self.pages) - 1
        await self.controller.edit(embed=self.pages[self.current])

      if response[0].emoji == self.reactions[1]:
        break

      if response[0].emoji == self.reactions[2]:
        self.current = self.current + 1 if self.current < len(self.pages) - 1 else 0
        await self.controller.edit(embed=self.pages[self.current])

    await self._close_session()

      
