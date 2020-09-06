"""
Pukage
Choose-your-own-adventure game.
https://github.com/Yourself1011/Pukage/

Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin, and all Pukage contributors https://github.com/Yourself1011/Pukage/graphs/contributors/

MIT License
"""

from scrolltype import scrolltype
from time import sleep
import re

waitTime = 0.2


def waittype(*text: str):
    """Scrolltypes text, then waits for an amount of time, then generates new lines."""

    for paragraph in text:
      if re.match('---sleep-\d+---$', paragraph) == None:
        scrolltype(paragraph)
        time = len(paragraph.split()) * waitTime
        scrolltype("\n\n")
        sleep(time)
      else:
        sleep(int(paragraph[9:3]))
