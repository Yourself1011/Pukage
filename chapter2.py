"""
Pukage
Choose-your-own-adventure game.
Copyright 2020 Daniel Zhang, Jeffery Zang, Li Feng Yin
MIT License
"""

from random import randint
from time import sleep as timeSleep
import scrolltype
from scrolltype import scrolltype as scrollType
import waittype as WaitType
from waittype import waittype
from inventory import inv
from settings import gameSettings
import readchar.readchar
import readchar.key
from typing import List, Any
from os import system, name
from threading import Thread
from options import options
import sys


def tempEnd():
    """This is a temporary ending, please insert this at the end of any unfinished code during testing"""

    waittype("Suddenly, you get a violent nosebleed and fall unconscious. The end.")

    waittype("Also this is just a temporary ending so if you see this then congrats.")

    waittype("ok bye")

    sys.exit()


def Chapter2intro(endThing):
    """does the intro for chapter 2"""
    waittype(
        "Welcome to chapter 2  of Pukage. The previous chapter was just an introduction because you couldn't lose anything or die. Now you can. Things are about to get a lot more serious."
    )

    if endThing == "following man":
        follow2()
    else:
        leavingWithoutFollowingMan()


def follow2():
    """following the man out of your house"""
    waittype(
        "You stomp out into the street after the man. You see blurry shadows of other buildings and houses. He turns around and sees you following him."
    )

    waittype(
        "He starts to weave around buildings and into shadows, trying to shake you off his tail. You notice that the city is very quiet and clean. No lights or sounds anywhere."
    )

    waittype(
        "He does a few tight turns around some dark alleyways and you lose sight of him. You look around corners and on different streets, but there is no sign of the man."
    )

    waittype(
        "The air is calm and clean. The streets are flat and paved with bricks. There are no lights in windows or people anywhere."
    )

    waittype(
        "You wander around for a few more minutes, looking for the man. You see the faint outline of a lighthouse in the distance."
    )

    waittype(
        "Suddenly, you see something moving in the corner of your eye. You turn towards it and see the man enter a building in the distance."
    )

    options(
        ["Follow him into the building", "Keep exploring the town"], [follow3, explore],
    )


def follow3():
    """following the man into the building"""
    waittype(
        "You slowly walk towards the building when you see a light turn on inside. You see the man's silhouette appear for a second. "
    )

    waittype(
        "You go around the side of the building and reach the door where the man went in. The building is small but has multiple floors. The door is heavy like those you would find in a warehouse or lab."
    )

    waittype(
        "You hear the man mumbling to himself and making noise. You hear a small generator hum in the back. It makes a low rumbling sound and suddenly stops."
    )

    waittype(
        "The man stops and starts to walk toward the door. You realise that he will see you if you do not move."
    )

    options(
        [
            "Hide in the back of the building",
            "Hide in the front where the windows are",
            "Confront the man",
        ][hide3, hide4, confrontTheMan]
    )


def hide3():
    """Hiding in the back of the building when the man comes out to fix the generator"""
    tempEnd()


def hide4():
    """Hiding in the front of the building where the windows are when the man comes out to fix the generator"""
    tempEnd()


def confrontTheMan():
    """confronting the man when he comes out to fix the generator"""
    tempEnd()


def explore():
    """exploring the city"""
    waittype(
        "You decide to ingnore the man and explore the city. The lighthouse is to your left, the house you came from to your right, and the building the man went in in front of you."
    )

    waittype(
        "The building with the man is small but has multiple floors. The lighthouse and your house are quite far away. You see a light turn on in the man's building."
    )

    waittype(
        "Behind you, there is what seems to be an abandoned restaurant with a bank next to it."
    )

    options(
        [
            "Go into the building with the man",
            "Go to the lighthouse",
            "Go back to your house",
            "Go to the restaurant",
            "Go to the bank",
        ][follow3, lighthouse, backToHouse, restaurant, bank]
    )


def lighthouse():
    """going to explore the lighthouse"""
    tempEnd()


def backToHouse():
    """Going back to your house"""
    tempEnd()


def restaurant():
    """Going to the restaurant"""
    tempEnd()


def bank():
    """going to the bank"""
    tempEnd()


def leavingWithoutFollowingMan():
    """leaving the house without following the man"""

    waittype(
        "The wind outside hits you like a jet of icy water. You shiver and move the blanket draped around your neck to cover as much of your body as possible."
    )

    waittype(
        "You look around, but you can barely see anything. The only light sources come from the moon, hovering in the sky, and the stars, scattered across the night sky."
    )

    tempEnd()
