"""
Pukage
Choose-your-own-adventure game.
https://github.com/Yourself1011/Pukage/

Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng, and all Pukage contributors https://github.com/Yourself1011/Pukage/graphs/contributors/

MIT License
"""

from scrolltype import scrolltype
from time import sleep


waitTime = 0.2


def waittype(string):
    scrolltype(string)
    time = len(string.split()) * waitTime
    scrolltype("\n\n")
    sleep(time)
