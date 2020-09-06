"""
Pukage
Choose-your-own-adventure game.
https://github.com/Yourself1011/Pukage/

Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin, and all Pukage contributors https://github.com/Yourself1011/Pukage/graphs/contributors/

MIT License
"""

from random import randint, uniform
from time import sleep as timeSleep
import scrolltype
from scrolltype import scrolltype as scrollType
import waittype as WaitType
from waittype import waittype
from inventory import inv
import readchar.readchar
import readchar.key
from typing import List, Any, Dict
from os import system, name, path
import inspect
import threading
import sys
import levelEditor

stats = {
    "health": 100,
    "hunger": 100,
    "energy": 100,
    "attack": 50,
    "critChance": 10,
    "critMulti": 2,
    "defense": 10,
}

difficultyFactor = 1

character = " O \n\\|/\n |\n/ \\"

dead = False

cursorColour = "\u001b[36m"


def commitDie():
    from chapter2 import lastWords

    global dead
    dead = True
    scrollType(lastWords)
    createMenu(
        scrolltype.log
        + "You have lost all of your health wile playing and died. Thank you for playing. This game is still is alpha development, so there may be bugs. We encourage you to keep trying until you complete Pukage.",
        ["Retry", "See the credits", "Quit to menu", "Quit"],
        [intro, credits, startingMenu, 'sys.exit("You exited the game.")'],
    )


def gotHurt(amountLost):
    stats["health"] -= amountLost * difficultyFactor
    if stats["health"] <= 0:
        commitDie()
    elif stats["health"] <= 10:
        waittype("Your limbs are broken.")
    elif stats["health"] <= 25:
        waittype("You have scratches, bruises, and cuts all over your body")
    elif stats["health"] <= 50:
        waittype("You are at half health.")

    return amountLost * difficultyFactor


def healed(amountHealed):
	stats["health"] += amountHealed / difficultyFactor
	waittype("You healed " + amountHealed / difficultyFactor + ".")
	if stats["health"] >= 100:
		stats["health"] = 100


def gotTired(amountLost=3):
    stats["energy"] -= amountLost * difficultyFactor
    if stats["energy"] <= 10:
        waittype("You are very tired. You must find somewhere to sleep.")
    elif stats["energy"] <= 25:
        waittype("You are more tired now. You should find somewhere to rest soon.")
    elif stats["energy"] <= 50:
        waittype("You are getting tired, but not too much.")


def nightmareOver():
	clearConsole()
	waittype("Since you had a nightmare, you didn't as good of a night's sleep.")
	stats["energy"] - 10 * difficultyFactor


def slept(amountSlept):
	stats["energy"] += amountSlept / difficultyFactor
	waittype("You slept. You gained " + amountSlept / difficultyFactor + " energy while sleeping.")
	if stats["health"] >= 100:
		stats["health"] = 100
	if amountSlept / difficultyFactor <= 25:
		nightmareChance = randint(1,15)
	if nightmareChance == 1 or nightmareChance == 2:
		waittype("You are having a nightmare.")
		waittype('(The Nightmare) We bought an old house, my boyfriend and I. He\'s in charge of the "new" construction – converting the kitchen in to the master bedroom for instance, while I\'m on wallpaper removal duty. The previous owner papered EVERY wall and CEILING! Removing it is brutal, but oddly satisfying. The best feeling is getting a long peel, similar to your skin when you\'re peeling from a sunburn. I don\'t know about you but I kinda make a game of peeling, on the hunt for the longest piece before it rips. Under a corner section of paper in every room is a person’s name and a date. Curiosity got the best of me one night when I Googled one of the names and discovered the person was actually a missing person, the missing date matching the date under the wallpaper! The next day, I made a list of all the names and dates. Sure enough each name was for a missing person with dates to match. We notified the police who naturally sent out the crime scene team. I overhead one tech say "yup, it\'s human." Human? What\'s human? "Ma\'am, where is the material you removed from the walls already? This isn\'t wallpaper you were removing."') 
		nightmareOver()
	if nightmareChance == 3 or nightmareChance == 4:
		waittype("You are having a nightmare.")
		waittype('(The Nightmare) I hate it when my brother Charlie has to go away. My parents constantly try to explain to me how sick he is. That I am lucky for having a brain where all the chemicals flow properly to their destinations like undammed rivers. When I complain about how bored I am without a little brother to play with, they try to make me feel bad by pointing out that his boredom likely far surpasses mine, considering his confine to a dark room in an institution. I always beg for them to give him one last chance. Of course, they did at first. Charlie has been back home several times, each shorter in duration than the last. Every time without fail, it all starts again. The neighbourhood cats with gouged out eyes showing up in his toy chest, my dad\'s razors found dropped on the baby slide in the park across the street, mom\'s vitamins replaced by bits of dishwasher tablets. My parents are hesitant now, using "last chances" sparingly. They say his disorder makes him charming, makes it easy for him to fake normalcy, and to trick the doctors who care for him into thinking he is ready for rehabilitation. That I will just have to put up with my boredom if it means staying safe from him. I hate it when Charlie has to go away. It makes me have to pretend to be good until he is back.')
		nightmareOver()
	if nightmareChance == 5 or nightmareChance == 6:
		waittype("You are having a nightmare.")
		waittype("(The Nightmare) He awoke to the huge, insect like creatures looming over his bed and screamed his lungs out. They hastily left the room and he stayed up all night, shaking and wondering if it had been a dream.The next morning, there was a tap on the door. Gathering his courage, he opened it to see one of them gently place a plate filled with fried breakfast on the floor, then retreat to a safe distance. Bewildered, he accepted the gift. The creatures chittered excitedly.This happened every day for weeks. At first he was worried they were fattening him up, but after a particularly greasy breakfast left him clutching his chest from heartburn, they were replaced with fresh fruit. As well as cooking, they poured hot steamy baths for him and even tucked him in when he went to bed. It was bizarre.One night, he awoke to gunshots and screaming. He raced downstairs to find a decapitated burglar being devoured by the insects. He was sickened, but disposed of the remains as best he could. He knew they had just been protecting him.One morning the creatures wouldn't let him leave his room. He lay down, confused but trusting as they ushered him back into bed. Whatever their motives, they weren't going to hurt him. Hours later a burning pain spread throughout his body. It felt like his stomach was filled with razor wire. The insects chittered as he spasmed and moaned. It was only when he felt a terrible squirming feeling beneath his skin that he realised the insects hadn't been protecting him. They had been protecting their young.")	
		nightmareOver()
	if nightmareChance == 7:
		waittype("You are having a nightmare.")
		waittype('(The Nightmare) Everyone loves the first day of school, right? New year, new classes, new friends. It\'s a day full of potential and hope, before all the dreary depressions of reality show up to ruin all the fun. I like the first day of school for a different reason, though. You see, I have a sort of power. When I look at people, I can...sense a sort of aura around them. A colored outline based on how long that person has to live. Most everyone I meet around my age is surrounded by a solid green hue, which means they have plenty of time left. A fair amount of them have a yellow-orangish tinge to their auras, which tends to mean a car crash or some other tragedy. Anything that takes people "before their time" as they say. The real fun is when the auras venture into the red end of the spectrum, though. Every now and again I\'ll see someone who\'s basically a walking stoplight. Those are the ones who get murdered or kill themselves. It\'s such a rush to see them and know their time is numbered. With that in mind, I always get to class very early so I can scout out my classmates\' fates. The first kid who walked in was basically radiating red. I chuckled to myself. Too damn bad, bro. But as people kept walking in, they all had the same intense glow. I finally caught a glimpse of my rose-tinted reflection in the window, but I was too stunned to move. Our professor stepped in and locked the door, his aura a sickening shade of green.')
		nightmareOver()
	if nightmareChance == 8:
		waittype("You are having a nightmare.")
		waittype('(The Nightmare) It has been said that the definition of insanity is "doing the same thing over and over and expecting different results". I understand the sentiment behind the saying, but it\'s wrong.I entered the building on a bet. I was strapped for cash and didn\'t buy into the old legends of the hotel to begin with, so fifty bucks was more than enough to get me do it. It was simple. Just reach the top floor, the 45th floor, shine my flashlight from a window.The hotel was old and broken, including the elevator, so that meant hiking up the stairs. So up the stairs I went. As I reached each platform, I noted the old brass plaques displaying the floor numbers. 15, 16, 17, 18. I felt a little tired as I crept higher, but so far, no ghosts, no cannibals, no demons. Piece of cake.I can\'t tell you how happy I was as I entered that last stretch of numbers. I joyfully counted them aloud at each platform. 40, 41, 42, 43, 44, 44. I stopped and looked back down the stairs. I must have miscounted, so I continued up. 44. One more flight. 44. And then down ten flights. 44. Fifteen flights. 44.And so it\'s been for as long as I can remember. So really, insanity isn\'t doing something repeatedly and expecting different results. It\'s knowing that the results will never ever change; that each door leads to the same staircase, to the same number. It’s realizing you no longer fall asleep. It\'s not knowing whether you\'ve been running for days or weeks or years. It\'s when the sobbing slowly turns into laughter.')
		nightmareOver()
	if nightmareChance == 9 or nightmareChance == 10:
		waittype("You are having a nightmare.")
		waittype('My daughter woke me around 11:50 last night. My wife and I had picked her up from her friend Sally\'s birthday party, brought her home, and put her to bed. My wife went into the bedroom to read while I fell asleep watching the Braves game."Daddy," she whispered, tugging my shirt sleeve. "Guess how old I\'m going to be next month.""I don\'t know, beauty," I said as I slipped on my glasses. "How old?"She smiled and held up four fingers.It is 7:30 now. My wife and I have been up with her for almost 8 hours. She still refuses to tell us where she got them.')
		nightmareOver()
	if nightmareChance == 11 or nightmareChance == 12:
		waittype("You are having a nightmare.")
		waittype('(The Nightmare) He had been given the watch on his tenth birthday. It was an ordinary grey plastic wristwatch in every respect except for the fact that it was counting down. "That is all of the time you have left in the world, son. Use it wisely." And indeed he did. As the watch ticked away, the boy, now a man, lived life to the fullest. He climbed mountains and swam oceans. He talked and laughed and lived and loved. The man was never afraid, for he knew exactly how much time he had left.Eventually, the watch began its final countdown. The old man stood looking over everything he had done, everything he had built. 5. He shook hands with his old business partner, the man who had long been his friend and confidant. 4. His dog came and licked his hand, earning a pat on the head for its companionship. 3. He hugged his son, knowing that he had been a good father. 2. He kissed his wife on the forehead one last time. 1. The old man smiled and closed his eyes. Then, nothing happened. The watch beeped once and turned off. The man stood standing there, very much alive. You would think that in that moment he would have been overjoyed. Instead, for the first time in his life, the man was scared.')
		nightmareOver()
	if nightmareChance == 13 or nightmareChance == 14:
		waittype("You are having a nightmare.")
		waittype('(The Nightmare) When my sister Betsy and I were kids, our family lived for awhile in a charming old farmhouse. We loved exploring its dusty corners and climbing the apple tree in the backyard. But our favorite thing was the ghost.We called her Mother, because she seemed so kind and nurturing. Some mornings Betsy and I would wake up, and on each of our nightstands, we\'d find a cup that hadn\'t been there the night before. Mother had left them there, worried that we\'d get thirsty during the night. She just wanted to take care of us.Among the house\'s original furnishings was an antique wooden chair, which we kept against the back wall of the living room. Whenever we were preoccupied, watching TV or playing a game, Mother would inch that chair forward, across the room, toward us. Sometimes she\'d manage to move it all the way to the center of the room. We always felt sad putting it back against the wall. Mother just wanted to be near us.Years later, long after we\'d moved out, I found an old newspaper article about the farmhouse\'s original occupant, a widow. She\'d murdered her two children by giving them each a cup of poisoned milk before bed. Then she\'d hanged herself.The article included a photo of the farmhouse\'s living room, with a woman\'s body hanging from a beam. Beneath her, knocked over, was that old wooden chair, placed exactly in the center of the room.')
		nightmareOver()
	if nightmareChance == 15:
		waittype("You are having a nightmare.")
		waittype('(The Nightmare) On Monday, I came up with the perfect plan. No one even knew we were friends.On Tuesday, he stole the gun from his dad.On Wednesday, we decided to make our move during the following day\'s pep rally.On Thursday, while the entire school was in the gym, we waited just outside the doors. I was to use the gun on whoever walked out first. Then he would take the gun and go into the gym blasting.I walked up to Mr. Quinn the guidance counselor and shot him in the face three times. He fell back into the gym, dead. The shots were deafening. We heard screams in the auditorium.No one could see us yet. I handed him the gun and whispered, "your turn." He ran into the gym and started firing. I followed a moment after.He hadn\'t hit anyone yet. Kids were scrambling and hiding. It was mayhem.I ran up behind him and tackled him. We struggled. I wrenched the gun out of his hands, turned it on him, and killed him. I closed his mouth forever. On Friday, I was anointed a hero. It was indeed the perfect plan.')
		nightmareOver()


def gotHungry(amountLost=0):
    stats["hunger"] -= amountLost * difficultyFactor
    if stats["hunger"] <= 0:
        waittype(
            "You are starving, and beginning to lose health. Eat to prevent extra health loss, or you will die."
        )
        gotHurt(5 * difficultyFactor)
    elif stats["hunger"] <= 10:
        waittype("You are extremely hungry. Eat food soon.")
    elif stats["hunger"] <= 25:
        waittype("Your stomach is rumbling.")
    elif stats["hunger"] <= 50:
        waittype("You are beginning to get hungry.")


def ate(amountAte):
	stats["hunger"] += amountAte / difficultyFactor
	waittype("You ate. You gained " + amountAte / difficultyFactor + " hunger points.")
	if stats["hunger"] >= 100:
		stats["hunger"] = 100


def showStats():
    bars = []
    barColours = ["\u001b[31m", "\u001b[33m", "\033[93m"]
    for i in range(3):
        thisBar = [barColours[i]]
        for j in range(round(list(stats.values())[i] / 10)):
            thisBar.append("■")
        thisBar.append("\u001b[0m")
        for k in range(10 - round(list(stats.values())[i] / 10)):
            thisBar.append("□")
        bars.append("".join(thisBar))
    return "Health:      Hunger:      Energy:\n" + " | ".join(bars) + f"\n{inv.show()}"


def health(health, maxHealth):
    thisBar = ["\u001b[31m"]
    increment = round(maxHealth/10)
    for j in range(round(health / increment)):
        thisBar.append("■")
    thisBar.append("\u001b[0m")
    for k in range(round((maxHealth / increment) - (health / increment))):
        thisBar.append("□")
    return "".join(thisBar)


def sleep(time):
    timeSleep(time * WaitType.waitTime)


def options(options: List[Any], functions: List[Any], *statsLost):
    """Creates a story option"""

    if (len(statsLost) > 3):
        raise ValueError(f"There are only 3 stats. What are you thinking, passing in {len(statsLost)} stats?")

    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])

    filename = module.__file__

    if filename == "/home/runner/Pukage/chapter2.py" or difficultyFactor >= 2:
        if (statsLost):
            statFunctions = ["gotHurt", "gotHungry", "gotTired"]
            for i, stat in enumerate(statsLost):
                eval(f"{statFunctions[i]}({stat})")
                
        else:
            gotHurt(0)
            gotHungry(1)
            gotTired(99)

    scrollType("What do you do?\n")

    sleep(1)

    createMenu(
        "\n".join(scrolltype.log), options, functions, footertext=showStats(),
    )


def threeDots():
    sleep(1)
    scrollType("...", scrolltype.scrollSpeed)
    sleep(2)


def fight(stats: Dict, oppStats: Dict, oppName, oppChar):
    """oppStats needs health, maxDamage, critChance, critMulti, defense, escapeChance (more is better chance)"""
    global fightChoice
    characterArray = []
    displayCharacter = character
    fightChoice = ""
    message = ""
    oppMaxHealth = oppStats.copy()["health"]

    print(displayCharacter)

    sleep(10)

    if len(oppChar.split("\n")) > len(displayCharacter.split("\n")):
        repeat = len(oppChar.split("\n"))
        while True:
            if len(displayCharacter.split("\n")) <= len(oppChar.split("\n")):
                displayCharacter += "\n"
            else:
                break
    else:
        repeat = len(displayCharacter.split("\n"))
        while True:
            if len(displayCharacter.split("\n")) >= len(oppChar.split("\n")):
                oppChar += "\n"
            else:
                break

    for i in range(repeat):
        characterArray.append(
            displayCharacter.split("\n")[i]
            + "\u2067"
            + oppChar.split("\n")[i]
            + "\u2069"
        )

    while oppStats["health"] > 0 and not dead:

        if randint(1, 2) == 1:
            oppChoice = "attack"
        else:
            oppChoice = "defend"

        oppHealthBar = health(oppStats["health"], oppMaxHealth)
        healthBar = health(stats["health"], 100)

        characters = "\n".join(characterArray)

        createMenu(
            f"{oppName}:\n{oppHealthBar}\n\n{characters}\n\nYou:\n{healthBar}\n{message}",
            [
                "\u001b[31mAttack\u001b[0m",
                "\u001b[36mDefend\u001b[0m",
                "Use item",
                "Run away",
            ],
            [
                "global fightChoice\nfightChoice = 'attack'",
                "global fightChoice\nfightChoice = 'defend'",
                "None",
                "global fightChoice\nfightChoice = 'flee'",
            ],
        )

        crit = not bool(randint(0, stats["critChance"]))
        oppCrit = not bool(randint(0, oppStats["critChance"]))

        critMulti = round(
            uniform(stats["critMulti"] - 1, stats["critMulti"] + 1),
            len(str(stats["critMulti"]).replace(".", "")),
        )

        oppCritMulti = round(
            uniform(oppStats["critMulti"] - 1, oppStats["critMulti"] + 1),
            len(str(oppStats["critMulti"]).replace(".", "")),
        )

        critMsg = ""
        oppCritMsg = ""

        if crit:
            dmg = randint(1, stats["attack"]) * critMulti
            critMsg = f" and landed a critical hit! {critMulti}x damage"
        else:
            dmg = randint(1, stats["attack"])

        if oppCrit:
            oppDmg = randint(0, oppStats["maxDamage"]) * oppCritMulti

            oppCritMsg = f" and landed a critical hit! {oppCritMulti}x damage"
        else:
            oppDmg = randint(0, oppStats["maxDamage"])

        if fightChoice == "attack" and oppChoice == "attack":
            oppStats["health"] -= dmg
            gotHurt(oppDmg)

            message = f"You attacked {oppName}{critMsg}. {oppName} lost {dmg} health.\n{oppName} attacked you{oppCritMsg}. You lost {oppDmg} health."
        elif fightChoice == "attack" and oppChoice == "defend":

            if randint(0, oppStats["defense"]):
                gotHurt(dmg / 2)

                message = f"You attacked {oppName}{critMsg}, but they defended, so you lost {dmg / 2} health."

            else:
                oppStats["health"] -= dmg / 2

                message = f"You attacked {oppName}{critMsg}, but they defended, but their defense failed, so {oppName} lost {dmg / 2} health."
        elif fightChoice == "defend" and oppChoice == "attack":

            if randint(0, stats["defense"]):
                oppStats["health"] -= oppDmg / 2

                message = f"{oppName} attacked you{critMsg}, but you defended, so {oppName} lost {oppDmg / 2} health."
            else:
                gotHurt(oppDmg / 2)

                message = f"{oppName} attacked you{critMsg}, but you defended, but your defense failed, so you lost {oppDmg} health."
        elif fightChoice == "defend" and oppChoice == "defend":
            message = f"You and {oppName} both defended. Absolutely nothing happened"

        elif fightChoice == "flee":

            waittype(
                f"You run away, as fast as you can, as you realize you are no match for {oppName}."
            )
            while True:
                if not randint(0, oppStats["escapeChance"]):
                    waittype(
                        f"You flee succesfully, and {oppName} is nowhere to be seen"
                    )
                    break
                else:
                    oppCrit = not bool(randint(0, oppStats["critChance"]))

                    oppCritMulti = round(
                        uniform(oppStats["critMulti"] - 1, oppStats["critMulti"] + 1),
                        len(str(oppStats["critMulti"]).replace(".", "")),
                    )

                    if oppCrit:
                        oppDmg = randint(0, oppStats["maxDamage"]) * oppCritMulti

                        oppCritMsg = (
                            f" and landed a critical hit! {oppCritMulti}x damage"
                        )
                    else:
                        oppDmg = randint(0, oppStats["maxDamage"])

                    gotHurt(oppDmg)

                    waittype(
                        f"You run as fast as you can, but he catches up and hits you{critMsg}. You lost {oppDmg} health."
                    )

                sleep(1)

            break

    if oppStats["health"] <= 0:
        clearConsole()
        waittype(f"{message}\nYou won the fight! {oppName} has now been defeated.")

decodeDict = {
    readchar.key.UP: "UP",
    readchar.key.DOWN: "DOWN",
    readchar.key.ENTER: "ENTER",
    readchar.key.ESC: "ESC",
    readchar.key.RIGHT: "RIGHT",
    readchar.key.LEFT: "LEFT",
    readchar.key.BACKSPACE: "BACK",
}


def tempEnd():
    """This is a temporary ending, please insert this at the end of any unfinished code during testing"""

    waittype("Suddenly, you get a violent nosebleed and fall unconscious. The end.")

    waittype("Also this is just a temporary ending so if you see this then congrats.")

    waittype("ok bye")

    
def intro():
    """Does the intro"""
    threeDots()

    waittype(
        "Note: the inv.add() function is being rewritten to incorporate the createMenu() function. Please take notice that there will be nothing in the inventory."
    )

    waittype("Your eyes peek open slowly after a long, deep sleep.")

    waittype(
        "Your room is cold, and dark, and your thin blankets provide minimal warmth."
    )

    waittype(
        "You rummage around for the lights when suddenly you hear something outside."
    )

    options(
        ["Investigate", "Look for the lights"], [investigate, lights],
    )


def investigate():
    """investigate option"""

    waittype(
        "You feel your way to the window, opening it and peering outside. The night is calm and dark. Only the moonlight shines on the bare sidewalk."
    )
    waittype(
        "Suddenly, you see a black figure emerge from the shadows. You can tell it's a man from his facial features illuminated by the moonlight.  "
    )

    waittype("He starts to walk towards your house.")

    options(
        ["Watch the man", "Look for the lights"], [watch, lightsTwo],
    )


def lights():
    """Looking for lights"""

    waittype("You look for the lights.")

    waittype("*rummage rummage rummage*")

    threeDots()
    sleep(3)

    waittype(
        "You find the light switch, only to realize that after flicking it on, you are still surrounded in darkness."
    )

    waittype(
        "Before you could register your shock, you hear a quiet clicking noise immediately followed by a creak. You hear quiet footsteps on the first floor. A person might have just broke into your house."
    )

    options(
        ["Look for a flashlight", "Hide"], [findWeapon, hide],
    )


def watch():
    """Watching the man"""

    waittype(
        "The hooded figure walks slowly and silently toward your house. He leans against the wall and sinks into the shadows."
    )

    waittype("You hear him quietly rummaging in his bag and pulling something out.")

    waittype(
        "There is a small click as the front door is unlocked. It creaks as it opens, and then the weird man disappears into it."
    )

    options(
        ["Hide", "Look for the lights", "Try and find a weapon"],
        [hide, "lightsTwo(True)", findWeapon],
    )


def lightsTwo(*manInsideHouse):
    """Looking for lights when the man is inside"""

    if not manInsideHouse:
        manInsideHouse = False

    threeDots()

    waittype("You rummage around in search of the lights.")

    waittype("*rummage rummage rummage*")

    if not manInsideHouse:
        waittype(
            "You hear a quiet creak noise. You're sure that the man you saw earlier just picked open the front door. You hear the man's footsteps travelling towards the stairs as you desperately search around for the light switch."
        )

    else:
        waittype(
            "You hear the man inside the house. You hear his footsteps travelling towards the stairs as you start to get more and more desperate."
        )

    waittype(
        "After a long search, you finally find the lights, but you hear the man's footsteps starting to climb up the stairs. You're sure that he will notice if the lights turn on."
    )

    options(
        ["Hide", "Try to find a weapon", "Turn on the lights"],
        [hide, findWeapon, lightsOn],
    )


def hide():
    """Hiding from the man"""

    waittype(
        "You feel around the darkness, trying to find a hiding place. You hear the man slowly walking down the hallway towards the stairs."
    )

    waittype(
        "You bump into the edge of the bed, pain shooting up and down your shoulder. You hear the steps creaking as the man slowly walks up the stairs."
    )

    waittype(
        "The man suddenly stops. Seeing your chance, you dive under your bed and lay still."
    )

    waittype(
        "The man pulls a flashlight out of his bag. He aims it around the room, illuminating it in a bright light. You lay as still as possible and prays he does not see you. "
    )

    waittype(
        "You can see a long rifle strapped to his back. A mask is covering his face. He has a big bag on his shoulder. There is a knife on his belt. "
    )

    waittype(
        "He looks for a few seconds, then starts rummaging in the drawers. Not finding anything, he turns around swiftly and leaves. You can tell that he is quite dangerous."
    )

    options(
        ["Look for the lights", "Search the drawers", "Follow the man"],
        [lightsThree, searchDrawers, follow],
    )


def lightsOn():
    """Turning on the lights after man breaks in"""

    waittype("You hear the man start to walk up the stairs.")

    waittype(
        "You flick the light switch, but you are still surrounded in darkness after turning in on."
    )

    waittype(
        "The staircase steps creak as the man climbs them. You don't know what this man wants, but you are paralysed with fear as you try to decide what to do, and wonder why the lights don't work."
    )

    options(
        ["Look for a flashlight in the drawers", "Look around for hiding places"],
        [findWeapon, closet],
    )


def closet():
    """Trying to hide and hiding in the closet"""

    waittype(
        "You look around the room, trying to find a hiding place. Your heart is pounding furiously inside your ribs as you hear the man approach the top of the stairs."
    )

    waittype(
        "You bump into a cold, metal doorknob. You think its the door to the hallway until you hear the man's footsteps coming from behind you."
    )

    waittype(
        "Realizing you can hide in the closet you just found, you open the door softly and stumble inside."
    )

    if randint(1, 2) == 1:
        waittype(
            "As you feel around the closet, something sharp touches your feet. Looking down to see what it was, you bump your head on the wall and let out a yelp."
        )

        waittype(
            "You hear the man reach the top of the stairs. His footsteps are travelling faster than before. You hastily close the closet door and pray he didn't hear you."
        )

        waittype(
            "The closet is pitch-dark. You move your hands around the cold floor until you get pricked by the object, leaving a papercut on your finger. You grab it carefully around the handle."
        )

        inv.add("small knife")

        waittype("You hear the door creak slowly as the man enters the room.")

        waittype(
            "The floor of the closet glows yellow as his footsteps move around the room slowly, heading towards the closet that you're hiding in."
        )

        waittype(
            "Suddenly, the man opens the closet door. You're blinded by yellow light as he shines a flashlight at you. You hear him jump backward in shock."
        )

        waittype(
            "He shines the flashlight away from you so he can see you. You see mostly green as your eyes try to recover from the brightness they were just exposed to, but you can see his sharp, concentrated face and a thin rifle on his back."
        )

        waittype(
            "Suddenly, his eyes flash dangerously as he notices the knife in your hand. He withdraws a long knife from his pocket immediately and brings it to your neck. You're petrified in fright as he throws away the flashlight and takes your knife from your hand."
        )

        randomInt = randint(1, 4)

        if randomInt == 1:
            item = "a sock"
        elif randomInt == 2:
            item = "some batteries"
        elif randomInt == 3:
            item = "an elastic band"
        else:
            item = "nothing"

        waittype(
            "He grabs his flashlight, walks towards one of the drawers, and rummages through it, occassionally glancing at you. He does the same for the other dresser."
        )

        if randomInt == 4:
            waittype("Finding nothing, he turns around swiftly and leaves the room.")

        else:
            waittype(
                f"Finding nothing but {item}, he turns around swiftly and leaves the room."
            )

        waittype(
            "You spot a wardrobe that the man didn't look inside. As you walk out of the closet to look inside it, grateful that nothing bad had happened, you spot something shiny on the floor. As you walk forward to investigate, you realize it's the knife you found in the closet."
        )

        options(
            ["Follow the man", "Try and turn on the lights", "Search the wardrobe"],
            [
              follow, 
              lightsThree, 
              "waittype('You open the wardrobe and find nothing inside.')\noptions(['Follow the man', 'Try and turn on the lights'], [follow, lightsThree])"]
        )

    else:
        waittype(
            "You close the door hastily right before the door creaks open and the man walks into the room. You catch a glimpse of him and notice a thin rifle strapped to his back."
        )

        waittype(
            "The floor of the closet is illuminated in yellow light for a few seconds before it dims. You hear him rummage through the drawers and pray he doesn't look in the closet."
        )

        waittype(
            "After what felt like an eternity, the door creaks again and the man leaves the room, closing the door behind him."
        )

        options(
            ["Follow the man", "Try and turn on the lights"],
            [
                'waittype("You open the closet door slowly, not daring to make a sound.")\nfollow()',
                lightsThree,
            ],
        )


def findWeapon():
    """Trying to find a weapon while the man is inside"""

    waittype(
        "You open the windows as wide as you can, letting the moonlight fill up the room. You see a nightstand next to your bed. You find nothing in the first drawer, but you find a flashlight after you yank open the second."
    )

    waittype(
        "You hear the man walking up the stairs. The steps creak as he walks closer and closer to the top of the stairs."
    )

    options(
        ["Grab the flashlight", "Keep searching"],
        [continueWithFlashlight, keepSearching],
    )


def continueWithFlashlight():
    """Keep searching with the flashlight"""

    inv.add("flashlight")
    waittype(
        "You grab the flashlight and turn it on. You shine the light around and see a dresser next to the bed."
    )

    generate(
        ["a water bottle", "nothing", "some batteries", "a sock", "an elastic band"]
    )

    print(item)

    waittype(
        "You run over to the dresser and pull it open, finding " + item + " inside."
    )

    inv.add(item)

    waittype("You close the drawer. You hear the man reach the top of the stairs.")

    waittype(
        "You shine the flashlight around the room once more, spotting a wardrobe. Although it could contain useful tools and could be used as a hiding place, you think it would be hard to walk over there without the man noticing you."
    )

    options(
        ["Hide under the bed quickly", "Stay where you are", "Search the wardrobe"],
        [hide2, stay, searchWardrobe],
    )


def keepSearching():
    """Keep searching without the flashlight"""
    waittype(
        "You leave the flashlight and look around the room again. You see a nightstand with a single drawer next to the bed."
    )

    generate(["a paperclip", "nothing", "a bandage"], 3)

    waittype(
        "\nYou run over to the dresser and pull it open, finding " + item + " inside."
    )

    inv.add(item)

    waittype("You close the drawer. You hear the man reach the top of the stairs.")

    waittype(
        "You look around, scanning the room for other places that could potentially hold items."
    )

    waittype(
        "You spot a wardrobe in the corner of the room. But the man is now completely silent except for his footsteps, moving quicker and closer towards your bedroom door."
    )

    options(
        ["Hide under the bed", "Stay where you are", "Search the wardrobe"],
        [hide2, stay, searchWardrobe],
    )


def hide2():
    """Hiding under the bed after searching for a weapon"""

    waittype(
        "You hide under the bed and turn off your flashlight, gripping it tightly. The man slowly opens the door. He does not walk in."
    )

    waittype(
        "You see him take something out of his bag. The little light from the moon barely illuminates his face."
    )

    waittype(
        "He seems to sense something in the room. You can see his alert and focused face."
    )

    waittype(
        "He pulled a short rod out of his bag. He smacked it on his thigh, making it glow. He then threw the glowstick into the room. It landed right in front of you, immediately illuminating your face."
    )

    waittype(
        "The man sees you and pulls out a knife from his pocket. He slowly creeps toward the drawers while keeping an eye on you."
    )

    waittype(
        "He opens one of the drawers and rummages inside. He goes to the dresser and does the same. Finding nothing, he slowly turns around and leaves."
    )

    options(
        ["Search the wardrobe", "Follow the man", "Turn on the lights"],
        [searchWardrobe2, follow, lightsThree],
    )


def searchWardrobe2():
    """searching the wardrobe after the man leaves after hide2()/closet()"""

    waittype(
        "You hear the man shut the front door slowly behind him as he leaves your house."
    )

    waittype(
        "You peek out the window and see him run away, dissapearing into the shadows."
    )

    waittype("After he leaves, you open the wardrobe doors and look inside.")

    generate(
        ["a small dagger", "a tank of gasoline", "a bandage", "nothing", "a hairpin"]
    )

    waittype("You find" + item + " in the wardrobe.")

    inv.add(item)

    options(["Follow the man", "Look for the lights"], [follow, lightsThree])


def searchWardrobe():
    """searching the wardrobe while the man is at your door"""

    waittype(
        "You creep towards the wardrobe and open it. Suddenly, the man opens the door. He gasps in shock when he sees you. He pulls a small knife out of his pocket and thrusts it at you."
    )

    randInt = randint(1, 3)

    if randInt == 1:
        item = "small dagger"
    elif randInt == 2:
        item = "gasoline"
    elif randInt == 3:
        item = "nothing"

    waittype(
        "He pushes you away and onto the bed. You are frozen still with fright as he looks in the wardrobe and pulls out "
        + item
    )

    if randInt == 3:
        waittype("Finding nothing, he quickly turns around and leaves.")

    else:
        waittype(
            "He grabs the "
            + item
            + " and runs out of the room. You hear him stomp down the stairs and leave."
        )

    options(["Follow the man", "Search the drawers"], [follow, searchDrawers])


def stay():
    """Staying where you are as the man walks in"""

    waittype(
        "You stay still, ready to face the man as he comes in. Your entire body is trembling in fright as you hear the person approach the door."
    )

    waittype(
        "You hear the doorknob twist and the door squeak quietly. The man walks in slowly, illuminating the room with his flashlight. Your heart is pounding frantically."
    )

    waittype("He checks his surroundings as he walks in before his eyes land on you.")

    waittype(
        "He quickly pulls a sharp silver knife out of his pocket and flashes it in your direction. But he doesn't say a word and walks towards the wardrobe, his eyes still fixed on you."
    )

    waittype(
        "You are frozen to the spot, relieved that he didn't do anything bad to you. But you are anxious as you start to think that the next few days are only going to get worse."
    )

    waittype(
        "The man is rummaging through the wardrobe, occasionally turning around to look at you. You see a thin rifle on his back."
    )

    waittype(
        "He also searches the nightstand and the dresser. Finding nothing but a few batteries, he turns around and leaves the room without glancing back at you."
    )

    options(["Follow the man", "Search the drawers"], [follow, searchDrawers])


def searchDrawers():
    """searching the drawers after the man leaves"""

    waittype("You open the drawers and look inside for anything useful.")

    waittype("*rummage rummage rummage*")

    randInt = randint(1, 2)

    if randInt == 1:
        item = "nothing"
    else:
        item = "a sock"

    waittype("You find " + item + " in the drawer.")

    inv.add(item)

    options(["Follow the man", "Look for the lights"], [follow, lightsThree])


def follow():
    """following the man after hide() and after the man leaves"""
    waittype(
        "You tiptoe quietly towards the door, not daring to make a sound. You hear the man's footsteps moving quickly and quietly towards the stairs."
    )

    waittype(
        "You place a hand on the doorknob and twist it, but you wait until you hear the man's feet hit the first floor until you push the door open."
    )

    waittype(
        "You sneak out of your room, walking quickly down the hallway, not daring to make any sound."
    )

    waittype(
        "You hear the man leave the house, closing the door noisily behind him. You quicken your pace as your feet thump down the steps."
    )

    waittype(
        "He pushes open the front door and runs away. You follow him into the darkness."
    )

    endThing = "following man"

    endOfChapterOne(endThing)


def lightsThree():
    """looking for the lights after you hid from the man"""
    waittype("You rummage around the room, looking for the lights.")

    waittype("*rummage rummage rummage*")

    waittype(
        "You find the light switch and flick it on. You look around the room, surpised at how big it actually is."
    )

    waittype(
        "The wardrobe is open with nothing inside. There is a blanket on your bed, which you decide to take with you. You wrap it around your back like a robe."
    )

    waittype(
        "You open the door to the hallway and walk down the stairs. The house is bare, no decorations or furniture anywhere."
    )

    waittype("You reach the front door. You grasp the doorknob and take a deep breath.")

    waittype("You push open the door and step into the outside.")

    endThing = "not following man"

    endOfChapterOne(endThing)


def endOfChapterOne(endThing):
    """the end of chapter one"""

    from chapter2 import Chapter2intro

    Chapter2intro(endThing)


def credits():
    """Shows the credits for pukage"""
    createMenu(
        "   _____              _ _ _       \n  / ____|            | (_) |      \n | |     _ __ ___  __| |_| |_ ___ \n | |    | '__/ _ \/ _` | | __/ __|\n | |____| | |  __/ (_| | | |_\__ \\\n  \_____|_|  \___|\__,_|_|\__|___/ \n\n Developers: ",
        ["  1. Jeffrey Zang", "  2. Li Feng Yin", "  3. Daniel Zhang", "\nBack"],
        [jeffInfo, liFengInfo, danInfo, startingMenu],
        "Special thanks to the contributors over at https://github.com/Yourself1011/Pukage/graphs/contributors/ \n\n1. Luke-Zhang-04\n\nBeta/alpha testers: \n	1. The Devs \n	2. yogogiddap#1332	\n	3. Cookie's Older Brother \n	4. I have no idea aka XxMoonlightxX9872",
    )


def jeffInfo():
    createMenu(
        "Jeffrey's Contacts: \n\n	Email: zangj4548@wrdsb.ca \n	Discord: Larg Ank#4494 \n    Repl: @LargAnk	",
        ["Back"],
        [credits],
    )


def danInfo():
    createMenu(
        "Daniel's Contacts: \n\n	Email: d.zhang200788@gmail.com \n	Discord: Yourself#3987 \n    Repl: @DanielZhang3	",
        ["Back"],
        [credits],
    )


def liFengInfo():
    createMenu(
        "Li Feng's Contacts: \n\n	Email: yinl8409@wrdsb.ca \n	Discord: Cookie's Owner#6343 \n    Repl: @LiFengFeng	",
        ["Back"],
        [credits],
    )


def scrollMenu(
    headerText,
    menuTitles: List[Any],
    menuDescriptions: List[Any],
    functions: List[Any],
    footerText,
):
    """Like createMenu(), but is side to side, not up and down"""
    index = 0
    print(scrollReload(headerText, menuTitles, menuDescriptions, index, footerText))

    while True:
        c = readchar.readkey()

        if c in decodeDict:

            if "{}".format(decodeDict[c]) == "LEFT":
                if index != 0:
                    index -= 1
                    print(
                        scrollReload(
                            headerText, menuTitles, menuDescriptions, index, footerText
                        )
                    )
                else:
                    index = int(len(menuTitles) - 1)
                    print(
                        scrollReload(
                            headerText, menuTitles, menuDescriptions, index, footerText
                        )
                    )

            elif "{}".format(decodeDict[c]) == "RIGHT":
                if index != int(len(menuTitles) - 1):
                    index += 1
                    print(
                        scrollReload(
                            headerText, menuTitles, menuDescriptions, index, footerText
                        )
                    )
                else:
                    index = 0
                    print(
                        scrollReload(
                            headerText, menuTitles, menuDescriptions, index, footerText
                        )
                    )

            elif "{}".format(decodeDict[c]) == "BACK":
                settings()

            elif "{}".format(decodeDict[c]) == "ENTER":
                clearConsole()
                if type(functions[index]) == str:
                    try:
                        return eval(functions[index])
                    except SyntaxError:
                        return exec(functions[index])
                    break
                elif type(functions[index]) == list:
                    for func in functions[index]:
                        if type(func) == str:
                            try:
                                return eval(func)
                            except SyntaxError:
                                return exec(func)
                            break
                        else:
                            return func()
                else:
                    return functions[index]()


def scrollReload(
    headerText, menuTitles: List[Any], menuDescriptions: List[Any], index, footerText
):
    clearConsole()
    title = "◀   " + menuTitles[index] + "   ▶"
    return (
        headerText
        + "\n\n"
        + title
        + "\n\n"
        + menuDescriptions[index]
        + "\n\n"
        + footerText
    )


decodeDict = {
    readchar.key.UP: "UP",
    readchar.key.DOWN: "DOWN",
    readchar.key.ENTER: "ENTER",
    readchar.key.ESC: "ESC",
    readchar.key.RIGHT: "RIGHT",
    readchar.key.LEFT: "LEFT",
    readchar.key.BACKSPACE: "BACK",
}


def createMenu(
    headertext,
    menuitems: List[Any],
    functions: List[Any],
    footertext: str = "",
    clear: bool = True,
):
    """Does stuff"""

    global index, headerText, menuItems, footerText, originalMenuItems

    index = 0
    headerText = headertext
    menuItems = menuitems
    footerText = footertext
    originalMenuItems = menuitems.copy()
    reload()

    while True:
        c = readchar.readkey()

        if c in decodeDict:

            if "{}".format(decodeDict[c]) == "UP":
                if index != 0:
                    index -= 1
                    reload()
                else:
                    index = int(len(menuItems) - 1)
                    reload()

            elif "{}".format(decodeDict[c]) == "DOWN":
                if index != int(len(menuItems) - 1):
                    index += 1
                    reload()
                else:
                    index = 0
                    reload()

            elif "{}".format(decodeDict[c]) == "ENTER":
                if clear:
                    clearConsole()
                    scrolltype.log = []
                if type(functions[index]) == str:
                    try:
                        return eval(functions[index])
                    except SyntaxError:
                        return exec(functions[index])
                    break
                elif type(functions[index]) == list:
                    for func in functions[index]:
                        if type(func) == str:
                            try:
                                return eval(func)
                            except SyntaxError:
                                return exec(func)
                            break
                        else:
                            return func()
                else:
                    return functions[index]()


def reload():
    """reloads"""
    clearConsole()

    menuItems = originalMenuItems.copy()
    indexVal = menuItems[index]
    pointer = indexVal + cursorColour + " «\u001b[0m"

    menuItems.pop(index)
    menuItems.insert(index, pointer)

    print(headerText + "\n")
    print("\n".join(menuItems))
    print("\n" + footerText)


def clearConsole():
    """deletes everything"""
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def startingMenu():
    """creates the starting menu"""
    createMenu(
        "\u001b[33m  _____       _                    \n |  __ \     | |                   \n | |__) _   _| | ____ _  __ _  ___ \n |  ___| | | | |/ / _` |/ _` |/ _ \\\n | |   | |_| |   | (_| | (_| |  __/\n |_|    \__,_|_|\_\__,_|\__, |\___|\n                         __/ |     \n                        |___/      \u001b[0m",
        [
            "\u001b[32mStart game\u001b[0m",
            "\u001b[34mLevel editor\u001b[0m",
            "\u001b[30;1mSettings\u001b[0m",
            "\u001b[33;1mCredits\u001b[0m",
            "\u001b[31mExit game\u001b[0m",
        ],
        [intro, levelEditor.levelsMenu, settings, credits, 'sys.exit("You exited the game.")'],
        version,
    )


def generate(choices: List[Any], *numberOfChoices):
    """Generates items"""
    if not numberOfChoices:
        numberOfChoices = len(choices)
    tempChoices = choices.copy()
    randomChoices = []
    menuItemsList = []
    menuItemsFunctions = []
    global item
    item = ""

    for i in range(1, numberOfChoices):
        int = randint(0, numberOfChoices)
        print(tempChoices)
        print(randomChoices)
        randomChoices.append(tempChoices[int - 1])
        tempChoices.pop(int - 1)

    for i in range(0, numberOfChoices):
        menuItemsList.append(str(i + 1))
        menuItemsFunctions.append("item = '" + randomChoices[i - 1] + "'")
    print(menuItemsFunctions)

    scrollType("Choose a number")
    createMenu(
        "\n".join(scrolltype.log), menuItemsList, menuItemsFunctions, clear=False
    )

    print(item)

    scrolltype.log.append("")


def setScrollSpeed():
    """sets the scroll speed"""
    print(
        "This setting sets the time it takes between each letter. Choose a number between 0 and 10. Default is 5. Type back to go back to the menu."
    )
    while True:
        userInput = input()

        try:
            userInputInt = int(userInput)

            if userInputInt <= 10 and userInputInt >= 0:
                scrolltype.scrollSpeed = userInputInt / 100
                break
            else:
                clearConsole()
                print("Please choose a number between 1 and 10")
                setScrollSpeed()
        except ValueError:
            if userInput.lower() == "back":
                break
            else:
                clearConsole()
                print("Please choose a number between 1 and 10")
                setScrollSpeed()
    settings()


def setWaitTime():
    """sets the wait time"""
    print(
        "This setting changes the time it waits after every line. Choose a number between 0 and 10. Default is 5. Type back to go back to the menu."
    )
    while True:
        userInput = input()

        try:
            userInputInt = int(userInput)

            if userInputInt <= 10 and userInputInt >= 0:
                WaitType.waitTime = userInputInt / 10
                break
            else:
                clearConsole()
                print("Please choose a number between 1 and 10")
                setWaitTime()
        except ValueError:
            if userInput.lower() == "back":
                break
            else:
                clearConsole()
                print("Please choose a number between 1 and 10")
                setWaitTime()
    settings()


def setDifficulty():
    """sets the difficulty"""
    global difficultyFactor
    scrollMenu(
        "  _____  _  __  __ _            _ _         \n |  __ \(_)/ _|/ _(_)          | | |        \n | |  | |_| |_| |_ _  ___ _   _| | |_ _   _ \n | |  | | |  _|  _| |/ __| | | | | __| | | |\n | |__| | | | | | | | (__| |_| | | |_| |_| |\n |_____/|_|_| |_| |_|\___|\__,_|_|\__|\__, |\n                                       __/ |\n                                      |___/ ",
        ["Invulnerable", "Easy", "Normal", "Hard", "Insane"],
        [
            "You cannot die or lose health. Basically, you win no matter what.",
            "Feeling casual? This is the mode for you. You lose stats half as fast as normal.",
            "Normal. For normal people. This is the normal mode. Very normal. Not much else to say.",
            "This mode is harder. It's pretty hard. Twice as hard as normal. You don't get the invulnerability at the beginning.",
            "What are you even doing?",
        ],
        [
            "global difficultyFactor\ndifficultyFactor = 0",
            "global difficultyFactor\ndifficultyFactor = 0.5",
            "global difficultyFactor\ndifficultyFactor = 1",
            "global difficultyFactor\ndifficultyFactor = 2",
            "global difficultyFactor\ndifficultyFactor = 10",
        ],
        "Press backspace to go back",
    )
    settings()


def customCharacter():
    print('Type your character. Say "break" for line breaks')

    global character
    character = input().replace("break", "\n")

    settings()


def setCursorColour():
    createMenu(
        """   _____      _                      
  / ____|    | |                     
 | |     ___ | | ___  _   _ _ __ ___ 
 | |    / _ \| |/ _ \| | | | '__/ __|
 | |___| (_) | | (_) | |_| | |  \__ \ 
  \_____\___/|_|\___/ \__,_|_|  |___/""",
        [
            "\u001b[30mBlack\u001b[0m",
            "\u001b[31mRed\u001b[0m",
            "\u001b[32mGreen\u001b[0m",
            "\u001b[33mYellow\u001b[0m",
            "\u001b[34mBlue\u001b[0m",
            "\u001b[35mMagenta\u001b[0m",
            "\u001b[36mCyan\u001b[0m",
            "\u001b[37mWhite\u001b[0m",
            "\nBack",
        ],
        [
            "global cursorColour\ncursorColour = u'\\u001b[30m'",
            "global cursorColour\ncursorColour = u'\\u001b[31'",
            "global cursorColour\ncursorColour = u'\\u001b[32m'",
            "global cursorColour\ncursorColour = u'\\u001b[33m'",
            "global cursorColour\ncursorColour = u'\\u001b[34m'",
            "global cursorColour\ncursorColour = u'\\u001b[35m'",
            "global cursorColour\ncursorColour = u'\\u001b[36m'",
            "global cursorColour\ncursorColour = u'\\u001b[37m'",
            settings,
        ],
    )

    settings()


def settings():
    createMenu(
        "   _____      _   _   _                 \n  / ____|    | | | | (_)                \n | (___   ___| |_| |_ _ _ __   __ _ ___ \n  \___ \ / _ | __| __| | '_ \ / _` / __|\n  ____) |  __| |_| |_| | | | | (_| \__ \ \n |_____/ \___|\__|\__|_|_| |_|\__, |___/\n                               __/ |    \n                              |___/     ",
        ["Typing Speed", "Wait Time", "Difficulty", "Cursor Colour", "\nBack",],
        [setScrollSpeed, setWaitTime, setDifficulty, setCursorColour, startingMenu,],
        version,
    )


version = "v1.0.0-alpha"


# def pause():
#     timeSleep(1)
#     while True:
#         c = readchar.readchar()
#         if c == "p":

#             threading.Lock().acquire()
#             createMenu("  _____                         _ \n |  __ \                       | |\n | |__) __ _ _   _ ___  ___  __| |\n |  ___/ _` | | | / __|/ _ \/ _` |\n | |  | (_| | |_| \__ |  __| (_| |\n |_|   \__,_|\__,_|___/\___|\__,_|                                  ", ["Resume Game", "Options", "Quit to title", "Quit"], ["threading.Lock().release()", settings, startingMenu, "sys.exit('You left the game.')"])

# def readChar():
#     global charList
#     charList = [["ESC", pause], ["RIGHT", pause]]
#     while True:
#         c = readchar.readkey()
#         if c in decodeDict:
#             for i in charList.length:
#                 if charList[i][0] == c:
#                     charCheck = True
#                     function = charList[i][1]
#                     break
#             if charCheck:

#                 if type(function) == str:
#                     try:
#                             eval(function)
#                     except SyntaxError:
#                             exec(function)
#                     break
#                 elif type(function) == list:
#                     for func in function:
#                         if type(function == str):
#                             try:
#                                     eval(func)
#                             except SyntaxError:
#                                     exec(func)
#                             break
#                             func()
#                 else:
#                     function()


# readChar = threading.Thread(target=readChar)
# readChar.start()
# mainThread = threading.main_thread()

if __name__ == "__main__":
    startingMenu()
    