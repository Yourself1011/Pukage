"""
Pukage
Choose-your-own-adventure game.
Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin
MIT License
"""

from scrolltype import scrolltype
from time import sleep


waitTime = 0.24

def waittype(string):
    scrolltype(string);
    time = len(string.split()) * waitTime
    scrolltype("\n\n")
    sleep(time)


# waittype scrolltypes, then calculates the amount of words, then waits for that amount, then generates new lines(\n\n\n\n)
