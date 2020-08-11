"""
Pukage
Choose-your-own-adventure game.
https://github.com/Yourself1011/Pukage/

Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng, and all Pukage contributors https://github.com/Yourself1011/Pukage/graphs/contributors/

MIT License
"""

from random import randint
from time import sleep
import scrolltype
from scrolltype import scrolltype as scrollType
import waittype as WaitType
from waittype import waittype
from inventory import inv
import readchar.readchar
import readchar.key
from typing import List, Any
from os import system, name
from threading import Thread
from options import options
import sys
from main import (
    showStats,
    commitDie,
    gotHurt,
    gotTired,
    gotHungry,
    createMenu,
    tempEnd,
    options,
    clearConsole,
    reload,
    fight,
    stats,
)

global lastWords

lastWords = "i haven't died yet so yeah"


def Chapter2intro(endThing):
    """does the intro for chapter 2"""

    clearConsole()

    global goneThroughTrapDoor

    goneThroughTrapDoor = False

    waittype("Chapter 2")

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
        "Suddenly, you see something moving in the corner of your eye. You turn towards it and see the man enter a building in the distance."
    )

    options(["Follow the man", "Explore the town"], [follow3, explore])


def follow3():
    """following the man into the building"""
    waittype(
        "You slowly walk towards the building when you see a light turn on inside. You see the man's silhouette appear for a second."
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
        ],
        [hide3, hide4, confrontTheMan],
    )


def hide3():
    """Hiding in the back of the building when the man comes out to fix the generator"""
    waittype(
        "You quickly walk over to the back of the building, away from the generator. You hide behind some boxes and wait for the man. "
    )

    waittype(
        "The man walks opens the door with a loud creak and the man steps outside."
    )

    waittype(
        "He walks over to the generator and dumps some fuel into it. It starts humming again and the lights inside turn back on. "
    )

    waittype("The man walks back into the building.")

    global generatorFixed

    generatorFixed = True

    options(
        ["Try to find a way into the building", "Explore the city"],
        [tryingToGoIn, explore],
    )


def tryingToGoIn():
    """trying to find a way into the building after the man fixes the generator"""

    waittype(
        "You look around the building. There is a small trapdoor that is quite high up near the back. You think that it leads to the second floor. The window in the front doesn't look like it can open. The heavy door is unlocked, and there are some boxes in the back too."
    )  # oops long waittype

    options(
        [
            "Use the boxes to go into the trapdoor",
            "Climb onto the generator to get into the trapdoor",
            "Try and break the window",
            "Enter through the front door",
            "Explore the city",
            "Search the boxes",
        ],
        [
            getIntoTrapdoorWithBoxes,
            getIntoTrapdoorWithGenerator,
            breakWindow,
            enterThroughDoor,
            explore,
            searchBoxes,
        ],
    )


def getIntoTrapdoorWithBoxes():
    """trying to get into the trapdoor using the boxes"""
    waittype(
        "You move some boxes around and position them like a staircase. You climb up and open the trapdoor."
    )

    waittype(
        "You squeeze in and fall out the other side into a completely dark room. You rummage around for the lights and flick it on."
    )

    waittype(
        "The light blinds your eyes, a huge change then the pitch black darkness just seconds before. The whole room is covered with poster and maps, notes and experiments. There is a small bed in the corner and a very messy desk with lots of papers and a laptop."
    )

    waittype(
        "The room feels like a laboratory or an office. You see diagrams of the sun and earth all around. You see models of the solar system, stickers and posters of scienticic terms."
    )

    waittype(
        "You sit at the desk and reach for the computer when you hear the man walking up the stairs."
    )

    options(
        ["Exit through the trapdoor", "Try and find somewhere to hide"],
        [exitThroughTrapdoor, hide5],
    )


def exitThroughTrapdoor():
    """trying to leave through the trapdoor when the man comes in"""

    number = randint(1, 2)

    if number == 1:
        waittype(
            "You decide to leave through the trapdoor. You lower yourself down onto the boxes, then drop out of sight just as the man comes in."
        )
    else:
        waittype(
            "You quickly open the trapdoor and try to put your feet down onto the boxes. You accidentally kick one of them and fall to the ground in surprise."
        )

        gotHurt(5)

    waittype(
        "You quickly hide behind some of the boxes and lay still, your heart beating heavily. You hear the man walk in, take some things, and then turn off the lights and walk out."
    )

    global goneThroughTrapDoor

    goneThroughTrapDoor = True

    options(
        [
            "Try to get back into the building through the trapdoor",
            "Search the boxes",
            "Go in through the front door",
            "Break the front window",
            "Explore the city",
        ][goBackInThroughTrapdoor, searchBoxes, breakWindow, explore]
    )


def goBackInThroughTrapdoor():
    """going back in through the trapdoor"""
    tempEnd()


def hide5():
    """finding somewhere to hide when the man comes in"""
    waittype(
        "You look around for a hiding place and decide to hide behind the door. The man comes in and takes the laptop. Then, he turns out the lights and leaves."
    )

    waittype(
        "You wait under the desk for a few more minutes while the man goes back downstairs."
    )

    options(
        ["Search the room", "Exit through the trapdoor", "Exit through the door"],
        [searchRoom, exitThroughTrapdoor2, exitThroughDoor],
    )


def searchRoom():
    tempEnd()


def exitThroughTrapdoor2():
    tempEnd()


def exitThroughDoor():
    tempEnd()


def getIntoTrapdoorWithGenerator():
    """Trying to get into the trapdoor using the gen."""
    waittype(
        "You step onto the generator and try to pull yourself up. The generator is surprisingly sturdy."
    )

    waittype(
        "You reach for the top of the trapdoor and pull yourself up. Suddenly, the generator breaks of the wall and crashes to the ground."
    )

    waittype(
        "Your fingers slip off of the trapdoor's frame and you fall down with a loud thud."
    )

    waittype(
        'The man rushes out and points a knife at you threateningly. "You!" he says in a deep voice. "What are you doing here?"'
    )

    gotHurt(5)

    options(
        ["""say "I'm just...exploring?" """, "Try to fight the man"],
        [pleaseDontHurtMeImJustExploring, fightMan],
    )


def pleaseDontHurtMeImJustExploring():
    """saying pleaseDontHurtMeImJustExploring to the man"""
    tempEnd()


def fightMan():
    """trying to fight the man"""
    fight(stats, {"health": 50, "maxDamage": 10, "critChance": 25, "critMulti": 1.5}, "The man",  "0v0\n💪💪\n  ‖‖\n/ \\")
    tempEnd()


def breakWindow():
    """Breaking the window to get in"""
    waittype(
        "You walk over to the front of the building and duck under the window. You try to look for something to break the window with."
    )

    waittype(
        "You spot a small but sharp piece of loose brick on the road. You pick it up. It feels quite heavy."
    )

    options(
        [
            "Try and use the rock to break the window",
            "Wait for the man to leave first.",
        ],
        [breakWindow2, waitForMan],
    )


def breakWindow2():

    global lastWords

    lastWords = "You stand up quickly and swing the rock at the window. It shatters, but broken glass shards shoot directly into your face, mouth, and eyes."

    gotHurt(100)


def waitForMan():
    tempEnd()


def enterThroughDoor():
    """Going through the door to get in"""
    waittype(
        "You walk over to the door and pull on the handle. You push open the door and "
    )


def searchBoxes():
    """Searching the boxes"""
    waittype("You rummage through the boxes.")

    waittype("*rummage rummage rummage*")

    randomItem = randint(1, 3)
    randomFood = randint(1, 3)

    if randomItem == 1:
        item = "nothing"
    elif randomItem == 2:
        item = "a small wristwatch"
    else:
        item = "a lighter"

    if randomFood == 1:
        food = "an apple"
    elif randomFood == 2:
        food = "a loaf of bread"
    else:
        food = "a large stick of butter"

    waittype("In the first box, you found a " + item + ".")

    inv.add(item)

    waittype("In the second box, you found " + food + ". Would you like to eat it?")

    print("1. Eat")
    print("2. Don't eat.")
    choice = input()

    print(showStats())

    if choice == "1" or choice == "2":
        if food == "an apple":
            gotHungry(-20)
            amountGained = "20"
        elif food == "a loaf of bread":
            gotHungry(-30)
            amountGained = "30"
        elif food == "a large stick of butter":
            gotHungry(-30)
            amountGained = "40"

    waittype("You ate " + food + " and replenished " + amountGained + " hunger points.")

    options(
        [
            "Try and go through the trapdoor using the boxes",
            "Try and go through the trapdoor using the generator",
            "Try to break the window",
            "Try to go through the front door",
            "Explore the city",
            "Try and find another way in",
        ],
        [
            getIntoTrapdoorWithBoxes,
            getIntoTrapdoorWithGenerator,
            breakWindow,
            enterThroughDoor,
            explore,
            findAnotherWay,
        ],
    )


def findAnotherWay():
    """Tryin to find another way into the building"""
    tempEnd()


def hide4():
    """Hiding in the front of the building where the windows are when the man comes out to fix the generator"""

    waittype(
        "The man walks out the door just as you get out of sight. You hear metal banging, and see sparks."
    )

    global generatorFixed

    generatorFixed = bool(randint(0, 1))

    if generatorFixed:
        waittype(
            "The man grunts heavily, and stomps his foot in rage. Returns inside, slamming the door."
        )
        options(["Wait", "Go towards the generator", "Get in the building"])
    else:
        waittype(
            "The hum returns, and you see the lights in the building come back on."
        )
        waittype("Suddenly, you see the generator light up a brilliant blue. You see sparks spark out of it.")
        waittype("Frozen in awe, you stay still, until you see something moving. Suddenly, a huge blue spider jumps out from behind the generator. You are in shock.")
        options(["Fight the spider", "Run", "Yell for help"])

    tempEnd()


def confrontTheMan():
    """confronting the man when he comes out to fix the generator"""
    tempEnd()


def explore():
    """exploring the city"""
    waittype(
        "You decide to ignore the man and explore the city. The lighthouse is to your left, the house you came from to your right, and the building the man went in in front of you."
    )

    waittype(
        "The building with the man is small but has multiple floors. The lighthouse and your house are quite far away. You see a light turn on in the man's building."
    )

    waittype(
        "The building with the man is small but has multiple floors. The lighthouse and your house are quite far away. You see a light turn on in the man's building."
    )

    options(
        [
            "Go into the building with the man",
            "Go to the lighthouse",
            "Go back to your house",
            "Go to the restaurant",
            "Go to the bank",
        ],
        [follow3, lighthouse, backToHouse, restaurant, bank,],
    )


def backToHouse():
    """Going back home for some reason"""
    tempEnd()


def restaurant():
    """going to the restaurant"""
    tempEnd()


def lighthouse():
    """going to explore the lighthouse"""
    waittype("You start to walk over to the lighthouse.")

    waittype("*walk walk walk*")

    waittype(
        "You get closer to the lighthouse and notice some other buildings. One has a staircase that leads to the second floor. You also notice a dock, with sailboats, jetskis, and other big boats.")

    waittype(
        "You keep walking and notice that you have entered a small neighbourhood. The gate and fence around it has been compeletely demolished."
    )
    waittype(
        "You see large apartment buildings in the distance. The windows are shattered and the walls are crumbing. You see no sign of life."
    )

    waittype(
        "You notice that the sky is brighter here. You can see the lighthouse clearly. You notice that it is a one-way road and that it is paved with concrete instead of bricks."
    )

    options(
        [
            "Go to the lighthouse",
            "Go to the dock",
            "Go to the building with the outdoor staircase",
            "Go to the apartments",
            "Go to the bank",
            "Go to the restaurant",
            "Go to the building with the man",
            "Go back to your house",
        ],
        [
            lighthouse2,
            dock,
            staircaseBuilding,
            apartments,
            bank,
            restaurant,
            follow3,
            backToHouse,
        ],
    )


def lighthouse2():
    """actually going to the lighthouse"""
    waittype("")


def dock():
    """going to the dock"""
    tempEnd()


def staircaseBuilding():
    """Going to the staircaseBuilding"""
    tempEnd()


def apartments():
    """going to the apartments"""
    tempEnd()


def bank():
    """going to the bank"""
    tempEnd()


def leavingWithoutFollowingMan():
    """leaving the house without following the man"""

    waittype(
        "The air outside is cold, but calm You shiver and move the blanket draped around your neck to cover as much of your body as possible."
    )

    waittype(
        "You look around, but you can barely see anything. The only light sources come from the moon, hovering in the sky, and the stars, scattered across the night sky."
    )

    waittype(
        "You start to take a small walk around the city. You notice that everything is eerily clean."
    )

    tempEnd()
