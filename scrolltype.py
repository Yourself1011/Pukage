"""
Pukage
Choose-your-own-adventure game.
Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin
MIT License
"""

from time import sleep
from settings import gameSettings, terminalSize

log = []
scrollSpeed = 0.05


def scrolltype(
    text, time: float = None, sep: str = "", end: str = "", flush: bool = True
):

    if time == None:
        speed = scrollSpeed
    else:
        speed = time

    if gameSettings["fastmode"] == "yes":
        print(text)
        return

    for letter in list(text):
        print(f"{letter}{sep}", end=end, flush=flush)
        sleep(speed)
    print("")
    log.append(text)


if __name__ == "__main__":
    scrolltype("BRUH")
