"""
Pukage
Choose-your-own-adventure game.
Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin
MIT License

"""

from random import randint
from time import sleep
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
import sys
from main import showStats, commitDie, gotHurt, gotTired, gotHungry, createMenu, tempEnd, options


def Chapter2intro(endThing):
	"""does the intro for chapter 2"""

	global goneThroughTrapDoor

	goneThroughTrapDoor = False

	waittype("Chapter 2")

	if endThing == "following man":
		follow2()	
	else:
		leavingWithoutFollowingMan()


def follow2():
  """following the man out of your house"""
  waittype("You stomp out into the street after the man. You see blurry shadows of other buildings and houses. He turns around and sees you following him.")

  waittype("He starts to weave around buildings and into shadows, trying to shake you off his tail. You notice that the city is very quiet and clean. No lights or sounds anywhere.")
  
  waittype("He does a few tight turns around some dark alleyways and you lose sight of him. You look around corners and on different streets, but there is no sign of the man.")

  waittype("The air is calm and clean. The streets are flat and paved with bricks. There are no lights in windows or people anywhere.")

  waittype("You wander around for a few more minutes, looking for the man. You see the faint outline of a lighthouse in the distance.")

  waittype("Suddenly, you see something moving in the corner of your eye. You turn towards it and see the man enter a building in the distance.")

  options(["Follow the man", "Explore the town"], [follow3, explore])


def follow3():
	"""following the man into the building"""
	waittype("You slowly walk towards the building when you see a light turn on inside. You see the man's silhouette appear for a second.")

	waittype("You go around the side of the building and reach the door where the man went in. The building is small but has multiple floors. The door is heavy like those you would find in a warehouse or lab.")

	waittype("You hear the man mumbling to himself and making noise. You hear a small generator hum in the back. It makes a low rumbling sound and suddenly stops.")

	waittype("The man stops and starts to walk toward the door. You realise that he will see you if you do not move.")

	options(
			["Hide in the back of the building", "Hide in the front where the windows are", "Confront the man"],
			[hide3, hide4, confrontTheMan]
	)


def hide3():
	"""Hiding in the back of the building when the man comes out to fix the generator"""
	waittype("You quickly walk over to the back of the building, away from the generator. You hide behind some boxes and wait for the man. ")

	waittype("The man walks opens the door with a loud creak and the man steps outside.")

	waittype("He walks over to the generator and dumps some fuel into it. It starts humming again and the lights inside turn back on. ")

	waittype("The man walks back into the building.")

	global generatorFixed

	generatorFixed = True

	options(
		["Try to find a way into the building", "Explore the city"],
		[tryingToGoIn, explore]
	)


def tryingToGoIn():
	"""trying to find a way into the building after the man fixes the generator"""

	waittype("You look around the building. There is a small trapdoor that is quite high up near the back. You think that it leads to the second floor. The window in the front doesn't look like it can open. The heavy door is unlocked, and there are some boxes in the back too.") #oops long waittype

	options(
		["Use the boxes to go into the trapdoor", "Climb onto the generator to get into the trapdoor", "Try and break the window", "Enter through the front door", "Explore the city", "Search the boxes"],
		[getIntoTrapdoorWithBoxes, getIntoTrapdoorWithGenerator, breakWindow, enterThroughDoor, explore, searchBoxes]
	)


def getIntoTrapdoorWithBoxes():
	"""trying to get into the trapdoor using the boxes"""
	waittype("You move some boxes around and position them like a staircase. You climb up and open the trapdoor.")

	waittype("You squeeze in and fall out the other side into a completely dark room. You rummage around for the lights and flick it on.")

	waittype("The light blinds your eyes, a huge change then the pitch black darkness just seconds before. The whole room is covered with poster and maps, notes and experiments. There is a small bed in the corner and a very messy desk with lots of papers and a laptop.")

	waittype("The room feels like a laboratory or an office. You see diagrams of the sun and earth all around. You see models of the solar system, stickers and posters of scienticic terms.")

	waittype("You sit at the desk and reach for the computer when you hear the man walking up the stairs.")

	options(
		["Exit through the trapdoor", "Try and find somewhere to hide"],
		[exitThroughTrapdoor, hide5]
	)


def exitThroughTrapdoor():
	"""trying to leave through the trapdoor when the man comes in"""

	number = randint(1,2)

	if number == 1:
			waittype("You decide to leave through the trapdoor. You lower yourself down onto the boxes, then drop out of sight just as the man comes in.")
	else:
			waittype("You quickly open the trapdoor and try to put your feet down onto the boxes. You accidentally kick one of them and fall to the ground in surprise.")

			gotHurt(5)

	waittype("You quickly hide behind some of the boxes and lay still, your heart beating heavily. You hear the man walk in, take some things, and then turn off the lights and walk out.")

	goneThroughTrapDoor = True

	options(
		["Try to get back into the building through the trapdoor", "Search the boxes", "Go in through the front door", "Break the front window", "Explore the city"]
		[goBackInThroughTrapdoor, searchBoxes, breakWindow, explore]
		)


def goBackInThroughTrapdoor():
	"""going back in through the trapdoor"""
	tempEnd()


def hide5():
	"""finding somewhere to hide when the man comes in"""
	waittype("You look around for a hiding place and decide to hide behind the door. The man comes in and takes the laptop. Then, he turns out the ")
	

def getIntoTrapdoorWithGenerator():
	"""Trying to get into the trapdoor using the gen."""
	waittype("You step onto the generator and try to pull yourself up. The generator is surprisingly sturdy.")

	waittype("You reach for the top of the trapdoor and pull yourself up. Suddenly, the generator breaks of the wall and crashes to the ground. ")

	waittype("Your fingers slip off of the trapdoor's frame and you fall down with a loud thud.")

	waittype('The man rushes out and points a knife at you threateningly. "You!" he says in a deep voice. "What are you doing here?"')

	gotHurt(5)

	options(
		["""say "I'm just...exploring?" """, "Try to fight the man"],
		[pleaseDontHurtMeImJustExploring, fight]
	)


def pleaseDontHurtMeImJustExploring():
	"""saying pleaseDontHurtMeImJustExploring to the man"""
	tempEnd()


def fight():
	"""trying to fight the man"""
	tempEnd()


def breakWindow():
	"""Breaking the window to get in"""
	tempEnd()


def enterThroughDoor():
	"""Going through the door to get in"""
	waittype("You walk over to the door and pull on the handle. You push open the door and ")


def searchBoxes():
	"""Searching the boxes"""
	waittype("You rummage through the boxes.")

	waittype("*rummage rummage rummage*")

	randomItem = randint(1,3)
	randomFood = randint(1,3)

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

	waittype("In the firt box, you found a " + item + ".")

	inv.add(item)

	waittype("In the second box, you found " + food + ". Would you like to eat it?")

	print("1. Eat")
	print("2. Don't eat.")
	choice = input()

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
		["Try and go through the trapdoor using the boxes", "Try and go through the trapdoor using the generator", "Try to break the window", "Try to go through the front door", "Explore the city", "Try and find another way in"],
		[getIntoTrapdoorWithBoxes, getIntoTrapdoorWithGenerator, breakWindow, enterThroughDoor, explore, findAnotherWay]
	)

def findAnotherWay():
	"""Tryin to find another way into the building"""
	tempEnd()


def hide4():
    """Hiding in the front of the building where the windows are when the man comes out to fix the generator"""

    waittype("The man walks out the door just as you get out of sight. You hear metal banging, and see sparks.")#Now what? I can't think of anything else wadoo yoo mean

    global generatorFixed

    generatorFixed = bool(randint(0, 1))

    if generatorFixed:
        waittype("The man grunts heavily, and stomps his foot in rage. Returns inside, slamming the door.")
        options(["Wait", "Go towards the generator", "Get in the building"])
    else:
        waittype("The hum returns, and you see the lights in the building come back on.")
    
    tempEnd()

def waitForMan():
    """Wait for the man after he returns inside after failing to fix the generator"""
    tempEnd()


def confrontTheMan():
	"""confronting the man when he comes out to fix the generator"""
	tempEnd()


def explore():
	"""exploring the city"""
	waittype("You decide to ignore the man and explore the city. The lighthouse is to your left, the house you came from to your right, and the building the man went in in front of you.")

	waittype("The building with the man is small but has multiple floors. The lighthouse and your house are quite far away. You see a light turn on in the man's building.")

	waittype("Behind you, there is what seems to be an abandoned restaurant with a bank next to it.")

	options(
		["Go into the building with the man", "Go to the lighthouse", "Go back to your house", "Go to the restaurant", "Go to the bank"],
		[follow3, lighthouse, backToHouse, restaurant, bank]

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

	waittype("The air outside is cold, but calm You shiver and move the blanket draped around your neck to cover as much of your body as possible.")

	waittype("You look around, but you can barely see anything. The only light sources come from the moon, hovering in the sky, and the stars, scattered across the night sky.")

	waittype("You start to take a small walk around the city. You notice that everything is eerily clean")

	tempEnd()