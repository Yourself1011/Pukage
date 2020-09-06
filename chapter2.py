"""
Pukage
Choose-your-own-adventure game.
https://github.com/Yourself1011/Pukage/

Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin, and all Pukage contributors https://github.com/Yourself1011/Pukage/graphs/contributors/

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
    fight,
    stats,
    slept,
    healed,
    ate,
)

global lastWords

lastWords = "i haven't died yet so yeah"


def Chapter2intro(endThing):
    """does the intro for chapter 2"""

    clearConsole()

    global goneThroughTrapDoor
    goneThroughTrapDoor = False

    global sawMan

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
        ],
        [goBackInThroughTrapdoor, searchBoxes, breakWindow, explore],
    )


def goBackInThroughTrapdoor():
    """going back in through the trapdoor"""
    waittype(
        "You climb back onto the boxes and go into the trapdoor. The lights are off and it is pitch black inside."
    )

    options(["Turn on the lights", "Leave"][lightsOn2, leaveRoom])


def lightsOn2():
	"""turning on the lights in the trapdoor room"""
	tempEnd()


def leaveRoom():
	"""leaving the trapdoor room"""
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
        [
            "Search the room", "Exit through the trapdoor",
            "Exit through the door"
        ],
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
    waittype(
        "The man grunts and pulls you off of the ground. Are you part of the Red Horse Gang?"
    )

    waittype(
        '"Uhh...", you mutter.\n"Tell me!", says the man, taking a knife out of his pocket and puts it to your throat. "No!", you scream in horror.'
    )

    waittype(
        'The man lets you go and you fall down to the ground in fright. He pulls you back up and sits down next to you. "Sorry about that. We\'ve always got to make sure, y\'know?"'
    )

    waittype(
        '"Don\'t talk much, do you? Well, I guess I just put a knife to your throat, so. Why don\'t you come in for a bit, have a rest, eh?"'
    )

    options(["Go inside with the man", 'say, "No thanks."'])


def goInWithTheMan():
    waittype(
        "The man opens the door to the building and walks inside. You are in some kind of lab with a huge counter surrounding the whole room. There is a large table with many chairs, cans, plates, and paper on it."
    )

    waittype(
        "The man reaches into a small fridge under the counter and pulls out two drinks. He throws one to you and sits down at the table, brushing some papers onto the ground to make space."
    )

    waittype('"So! Where you from?", the man asks, taking a sip from his can.')

    cityCountry = input("Where are you from? (city,country)")

    waittype('"I\'m from ' + cityCountry + ' . What about you?"')

    waittype(
        '"I\'ve been here my whole life. This is my hometown.", said the man.')

    waittype('"Ok. What is this place, anyway?"')

    waittype(
        '"This is Farside. A town on the west coast of Quebec, near Hudson\'s Bay.", said the man. You open the can and take a sip. The cool, refreshing liquid reminds you how thirsty you are.'
    )

    waittype(
        '"Ahh...", said the man. "I think we got off on the wrong foot. Let\'s start over. My name\'s Daniel. People call me the Dan Man."'
    )

    waittype('"My name is..."')

    uName = input("What is your name?")

    waittype('"My name is"' + uName + '"."')

    waittype('"Well, it\'s kinda late now. Wanna stay the night?"')

    options(["Stay the night", 'say, "No thanks."'], [stay2, noThanks2])


def stay2():
    randomInt = randint(10, 100)
    slept(randomInt)
    if randomInt <= 25:
      waittype("\nYou wake up from your nightmare, scared but glad that it is over.")

    waittype("You were so tired last night that you fell asleep right away. You didn't notice anything in the large bedroom that you are in.")

    waittype("You remember Dan from last night. You are glad that he helped you. You look around and see a staircase leading downstairs, a small wardrobe, another door, 2 closed windows with blinds, and a small desk and chair in the corner.")
 
    options(["Go downstairs", "Open the wardrobe", "Go through the door", "Go over to the desk", "Look for the lights", "Open the windows"],[goDownstairs, searchWardrobe3, goThroughDoor, goToDesk, lights2, openWindows])


def goDownstairs():
	waittype("You get out of bed and start walking downstairs. Eerie paintings line the walls as you walk down. You enter the lab that you were in last night.")

	waittype("You see another door and walk through it, entering a kitchen area. You see a sign on the fridge that says: 'cook food pls'. You think the man is still sleeping upstairs, so you get some food from the fridge and start preparing breakfast.")

	waittype("You notice that it is still dark outside, even though you slept, but you don't think much of it. You eat the potatoes that you cooked and brew some coffee.")
	
	waittype("Daniel comes downstairs, looking tired and weary. He pours himself a cup of coffee and helps himself to the potatoes.")

	waittype('"Good morning,"he says.')

	waittype('"You too," you say.')

	waittype('The man swallows and says, "Hmm. This is really good. How did you learn to make it?"\n\n"Um, I\'ve always liked to cook."')

	waittype('"So, uh, do you have any other relatives?" asked Daniel. "Like, before all this, if you know what I mean."')

	waittype('"Before all this? Before what?"')

	waittype('"Well, before the Cactypus Engine failed, of course!" Daniel exclaimed.')

	waittype('"What? Cactypus Engine? What? What are you talking about?", you ask.')

	waittype('Daniel raises his eyebrows at you. Then, he notices a ring on your pinkie with the letter C engraved on it. "Are you... were you one of the scientists that survived? Are you the person Pam recued? Woah! I-I-I how! What? Wait, then you must know Pam, right?"')

	waittype('"What? Who\'s Pam? What are you talking about?"')

	waittype('Daniel pauses for a moment and takes a sip of coffee. "Ok. Let me tell you everything."')

	goDownstairsContinued()


def goDownstairsContinued():
	clearConsole()
	waittype('"About 300 years ago, in January of 2051, astronomers and scientists at NASA saw a large asteroid speeding towards Earth. The asteroid was predicted to come close to Earth, but not come in contact with it." Daniel paused and thinked.')

	waittype('"This was a long time ago, obviously before you or I were born. The disease of 2020 had long since ended, and everything seemed to be going perfectly. People were inventing new things, self-driving cars were mass-produced, everything was fine. Until it wasn\'t."')

	waittype('"When the asteroid came closer, scientists noticed that it was getting pulled toward Earth by gravity. Everyone panicked and it was like the pandemic all over again."')

	waittype('"It sped up too quickly and there was no way to stop it. Eventually, it hit right in the Middle East, damaging lots of Asia, Europe, and Africa. Large shockwaves went on for days, the Earth\'s population was almost halved, and it was knocked out of the Sun\'s gravitational pull, speeding out of the solar system."')

	waittype("Daniel took another sip of his coffee and made a disgusted face.")

	clearConsole()

	waittype('"Everyone was terrified. Millions of people died, but a very very smart group of scientists, mechanics, and computer programmers designed and made the Cactypus Engine, a 500,000,000 megawatt engine powered by the sun, the wind, and all of the shockwaves left over from the asteroid."')

	waittype('"The Cactypus Engine was finished in 6 months, and was immediately put to use. It created mass so that the large dent left in the Earth by the asteroid was filled in. Then, the Earth would have enough mass to be able to orbit around the sun properly."')

	waittype('"For decades, the Cactypus Engine kept the Earth in place and everyone lived happily. The population went back up, and the asteroid dent left in the Earth slowly became habitable. Everything seemed fine. Until it wasn\'t."')

	waittype('"Around 3 years ago, a group of former terrorists came together to create the Red Horse Gang, with the goal of causing nothing but chaos and destruction."')

	waittype('"At first, they just looted shops and scared old people. But slowly, they grew into bigger and bigger. One day, they came up with something really really evil. They would destory the Cactypus Engine."')

	waittype("Daniel gets some cheese from the fridge and puts it into the microwave. He waits for a couple seconds, scoops the melted cheese out of the microwave with his hand, and slurps it up, leaving the excess cheese still inside the microwave.")

	clearConsole()

	waittype('Daniel continues. "They had a group of the most evil Red Horse People build an insane weapon to destory the engine. All of the people working on it had a ring just like yours. When the explosion happened, many people died, but some lucky scientists survived but lost their memories."')

	waittype('"After the Cactypus Engine stopped working, the Earth flew away from the sun and is now just floating around in the solar system towards Jupiter, which is why it\'s always dark here."')

	waittype('"Many people died, either from the heat of the sun or the cold of the night every day. The world seemed like it would collapse. But one day, Pam and 3 others decided to try and hunt down the Red Horse Gang themselves. They got me to come, too. We called it Operation Pukage."')

	waittype('"We had tracked the Red Horse Gang\'s headquarters to here in Farside. All 10 of us moved into this building. We were up 24 hours a day, researching, looking through old abandoned libraries and things. Suddenly, all of our teammates except for Pam and I disappeared. We were really scared, because it meant that they were onto us. We were much more careful, wearing masks and staying away from people."')

	waittype("Daniel stood up and walked around the room.")

	clearConsole()

	waittype('"One night, Pam went took the small plane that we had and flew to where the Cactypus Engine was. Miraculously, she found you there! She immediately brought you back to your old house, where you woke up yesterday. Right after she got back, she got a call from someone who said that they knew where our missing coworkers were. She called to tell me that she was going to find them. She left immediately."')

	waittype("Daniel paused for a moment, thinking, and took a sip of your coffee, making a satisfied face instead of a disgusted one.")

	waittype('"When I went to do the daily looting, I went to your house to look for supplies, just like I do on a regular basis. Pretty soon we\'re gonna have to move out of the city since the  things are running low. I know someone who\'s importing things from the sOuTh down by the river."')

	waittype("Anyway, I was searching your house when you woke up there. You followed me back, and here we are.")

	waittype('You sit there for a moment, stunned by everything he has just said. He takes another sip of your coffee.')

	options(['ask, "Where is Pam now?"', 'ask, "So...can I help?"'],[wherePam, iHelpPls])


def wherePam():
		waittype('"So...where is Pam?" you ask. Daniel pauses for a moment and sighs. "She...hasn\'t come back." Your eyes grow big in horror. "We...we must try and find her!" you exclaim.')

		waittype('"Yeah...I\'ve tried, but nothing not even a single clue. The only thing she said was that she was going to a factory of some sort."')

		waittype('You look at the clock and realizes that it is noon already. "Oh!" Daniel says. "I better get going." He gets up and goes into the lab room. He rummages around for something. Suddenly, you have an idea. "Hey! I could help you find Pam!"')

		waittype('Daniel perked up. "Woah! Why didn\'t I think of that! Of course you can help! Ok, ok, we\'ll get started right away." He seemed to have a big burst of enthusiasm. You smile to yourself. Or maybe it was just the coffee.')

		sleep(3)

		waittype("After taking a very short shower and changing clothes, you and Daniel go down to the lab to pick up some supplies.")

		waittype('"So," Daniel says. "I think we should try to explore the city today and see if we can find the factory with Pam, or see if we can find where the little trade route is."')

		options(['Try and find Pam', 'Try and find the trading route'],[letsfindpam, traderoute])


def letsfindpam():
	tempEnd()


def traderoute():
	tempEnd()


def iHelpPls():
	tempEnd()


def searchWardrobe3():
	tempEnd() 


def goThroughDoor():
	tempEnd()


def goToDesk():
	tempEnd()


def lights2():
	tempEnd()


def openWindows():
	tempEnd()


def noThanks2():
    tempEnd()


def noThanks():
    tempEnd()


def fightMan():
    """trying to fight the man"""
    fight(
        stats, {
            "health": 100,
            "maxDamage": 25,
            "critChance": 25,
            "critMulti": 2,
            "defense": 25,
            "escapeChance": 2,
        })
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

    waittype("In the second box, you found " + food +
             ". Would you like to eat it?")

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

    waittype("You ate " + food + " and replenished " + amountGained +
             " hunger points.")

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
    """Trying to find another way into the building"""
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
        waittype(
            "Suddenly, you see the generator light up a brilliant blue. You see sparks spark out of it."
        )
        waittype(
            "Frozen in awe, you stay still, until you see something moving. Suddenly, a huge blue spider jumps out from behind the generator. You are in shock."
        )
        options(["Fight the spider", "Run", "Yell for help"])

    tempEnd()


def confrontTheMan():
    """confronting the man when he comes out to fix the generator"""
    tempEnd()


def explore():
    """exploring the city"""
    waittype("You decide to ignore the man and explore the city.")

    waittype(
        "You come to a fork in the road. The path to the left leads to a lighthouse while a bank and a restaurant are towards your right. The path in front of you leads to the building the man went in."
    )

    waittype(
        "The building where the man went is small but has multiple floors. The lighthouse and the house you came from are quite far away. You see a light turn on in the man's building."
    )

    waittype(
        "The building with the man is small but has multiple floors. The lighthouse and your house are quite far away. You see a light turn on in the man's building."
    )

    options(
        [
            "Go into the building with the man",
            "Go to the lighthouse",
            "Turn back and return to your house",
            "Go to the restaurant",
            "Go to the bank",
        ],
        [follow3, lighthouse, backToHouse, restaurant, bank],
    )


def backToHouse():
    """Going back home for some reason"""
    tempEnd()


def restaurant():
    """going to the restaurant"""

    waittype(
        "You decide to take the right fork and head towards the restaurant.")

    waittype(
        "You hear your footsteps rapping against the dirt path. You see the restaurant and the bank in the distance. You reach a road and hear your feet hit the tarmac."
    )

    waittype(
      "You keep walking along the road, your feet barely making any sound. As you near the parking lot, you notice that the windows of both buildings are smashed and glass shards litter the ground."
    )

    waittype(
      "You step inside the parking lot, which stretches around the entire building. But all of a sudden, you hear voices coming from the back of the restaurant.")


    options([
        "Investigate the noise", "Hide", "Enter the restaurant"
        "Turn back and run"
    ], 
    [
        investigateNoise, hideNearRestaurant, enterRestaurant,
        runFromRestaurant
    ])


def investigateNoise():
    """Investigating noise coming from the back of the restaurant"""

    waittype(
        "You sneak towards the back of the restaurant, dodging the glass pieces being illuminated by the bright moon. You poke your head around the corner and see..."
    )

    tempEnd()


def hideNearRestaurant():
    """Searching for hiding places near the restaurant"""

    waittype(
        "You scan the area for hiding places. You see some thorny bushes near the parking lot where you are. The bushes are thick with green leaves and thorns. It might be able to conceal you."
    )

    waittype(
        "You notice you can't see the restaurant interior because its pitch-dark and no lights are turned on. It would be a good place to hide, as long as nobody enters the restaurant."
    )

    waittype(
        "The voices amplify in sound."
    )

    options([
        "Hide in the bushes", "Stay where you are", "Enter the restaurant",
        "Turn back and run"
    ], [hideInBushes, stayAtRestaurant, enterRestaurant, runFromRestaurant])


def hideInBushes():
    """Hiding in some bushes near the restaurant"""

    waittype(
        "You sneak towards a cluster of green bushes, making sure the person or people at the back of building can't see you."
    )

    waittype(
        "You drop to your knees and bury yourself in the bushes. The sharp thorns scratch your skin. You wince in pain."
    )

    gotHurt(2)

    waittype(
      "You try to see through the green thorns and bushes. You can see the outline of a person, who seems to be the leader, speaking to a large group of people.",

      "You can barely hear them, but you catch a phrase every now and then.",

      "...yeah, that's true...",

      "...the Earth...",

      "...don't know why...",

      "...Red Horse Gang...",

      
    )

    tempEnd()


def runFromRestaurant():
		"""Running away from restaurant"""
		
		if (randint(1, 3) == 1):
			waittype(
				"You turn around and run as fast as your legs could carry you. You reach the dirt path and slip because you ran too fast. You scrape your knee."
			)
		

			hurtAmount = gotHurt(randint(1, 5))

			if hurtAmount < 5:
				waittype(
					"You look at your knee. You see a faint white line where you fell. You get up and look behind you, nothing in sight.",

					"You walk at a fast pace, looking at the lighthouse in the distance. You reach the same fork in the road that you saw earier."
				)
			
			else:
				waittype(
					"You examine your knee, which is pink and bleeding. "
				)
		else:
			tempEnd()
    #options([follow3, lighthouse, backToHouse, restaurant, bank]) #uh
    


def stayAtRestaurant():
    
    waittype("")


def enterRestaurant():
    """Entering the restaurant"""

    waittype(
        "You head towards the door of the restaurant, situated near the left side of the building."
    )


def lighthouse():
    """going to explore the lighthouse"""
    waittype("You start to walk over to the lighthouse.")

    waittype("*walk walk walk*")

    waittype(
        "You get closer to the lighthouse and notice some other buildings. One has a staircase that leads to the second floor. You also notice a dock, with sailboats, jetskis, and other big boats."
    )

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

    waittype("Suddenly, you hear a noise")
