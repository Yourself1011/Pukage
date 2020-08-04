"""
Pukage
Choose-your-own-adventure game.
https://github.com/Yourself1011/Pukage/
Copyright 2020 Daniel Zhang, Jeffery Zang, Li Feng, and all Pukage contributors https://github.com/Yourself1011/Pukage/graphs/contributors/
MIT License
"""

from subprocess import call
import os
from time import sleep


def scrolltype(
    text, time: float = 0.1, sep: str = "", end: str = "", flush: bool = True
):
    for letter in list(text):
        print(f"{letter}{sep}", end=end, flush=flush)
        sleep(time)
    print("")


def clear():
    _ = call("clear" if os.name == "posix" else "cls")


terminalSize = os.get_terminal_size()


gameSettings = {
    "fastmode": {
        "name": "fastmode",
        "options": ["yes", "no"],
        "info": "Fastmode will disable any type of waiting, like scroll typing, so you can read at your own pace.",
    }
    #
}
