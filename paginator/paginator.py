# <=>  Naomi-Bot-Open-Source Project <=>
# Simple to use embed paginator with reaction control

from discord import Embed
from discord.ext.commands import Context
from asyncio import TimeoutError


class Paginator:
  def __init__(self, ctx: Context):
    self.reactions = ('⬅', '⏹', '➡')
    self.pages = []
    self.current = 0
    self.ctx = ctx


  async def _close_session(self):
    await self.controller.delete()
    del self.pages
    del self.reactions
    del self.current
    del self.ctx


  def add_page(self, embed: Embed):
    """ Add new page to paginator """
    self.pages.append(embed)


  async def call_controller(self, start_page: int = 0):
    if start_page > len(self.pages) - 1:
      raise IndexError(f'Currently added only {len(self.pages) - 1} pages,\
        but you tried to call controller with start_page = {start_page}')
        
    self.controller = await self.ctx.send(embed=self.pages[start_page])

    for emoji in self.reactions:
      await self.controller.add_reaction(emoji)

    while True:
      try:
        response = await self.ctx.bot.wait_for('reaction_add', timeout=120,
          check=lambda r, u: u.id == self.ctx.author.id and r.emoji in self.reactions\
            and r.message.id == self.controller.id)
      except TimeoutError:
        break
      
      await self.controller.remove_reaction(response[0], response[1])                  
      
      if response[0].emoji == self.reactions[0]:
        self.current = self.current - 1 if self.current > 0 else len(self.pages) - 1
        await self.controller.edit(embed=self.pages[self.current])

      if response[0].emoji == self.reactions[1]:
        break

      if response[0].emoji == self.reactions[2]:
        self.current = self.current + 1 if self.current < len(self.pages) - 1 else 0
        await self.controller.edit(embed=self.pages[self.current])

    await self._close_session()

      