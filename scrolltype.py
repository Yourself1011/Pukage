"""
Pukage
Choose-your-own-adventure game.
https://github.com/Yourself1011/Pukage/

Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin, and all Pukage contributors https://github.com/Yourself1011/Pukage/graphs/contributors/

MIT License
"""

from time import sleep

log = []
scrollSpeed = 0.05


def scrolltype(
    text, waittime: float = None, sep: str = "", end: str = "", flush: bool = True
):

    if waittime == None:
        speed = scrollSpeed
    else:
        speed = waittime

    for letter in list(text):
        print(f"{letter}{sep}", end=end, flush=flush)
        sleep(speed)
    print("")
    log.append(text)


if __name__ == "__main__":
    scrolltype("BRUH")
