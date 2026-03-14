
import asyncio

from kivy.app import async_runTouchApp
from kivy.uix.label import Label

loop = asyncio.get_event_loop()
loop.run_until_complete(
  async_runTouchApp(Label(text='Hello, World!'), async_lib='asyncio'))
loop.close()


"""

import trio

from kivy.app import async_runTouchApp
from kivy.uix.label import Label

from functools import partial

# use functools.partial() to pass keyword arguments:
async_runTouchApp_func = partial(async_runTouchApp, async_lib='trio')

trio.run(async_runTouchApp_func, Label(text='Hello, World!'))

"""
