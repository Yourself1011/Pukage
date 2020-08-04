"""
Pukage
Choose-your-own-adventure game.
https://github.com/Yourself1011/Pukage/
Copyright 2020 Daniel Zhang, Jeffery Zang, Li Feng, and all Pukage contributors https://github.com/Yourself1011/Pukage/graphs/contributors/
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
import threading
import sys


def sleep(time):
    timeSleep(time * WaitType.waitTime)


def options(options, functions):
    scrollType("What do you do?\n")

    sleep(1)

    createMenu(
        "\n".join(scrolltype.log), options, functions,
    )


def threeDots():
    sleep(1)
    scrollType("...", WaitType.waitTime)
    sleep(2)


def intro():
    """Does the intro"""
    threeDots()

    waittype("Your eyes peek open slowly after a long, deep sleep.")

    waittype(
        "Your room is cold and dark, and your thin blankets provide minimal warmth."
    )

    waittype(
        "You rummage around for the lights when suddenly you hear something outside."
    )

    scrollType("What do you do?\n")

    createMenu(
        "\n".join(scrolltype.log),
        ["Investigate", "Look for the lights"],
        [investigate, lights],
    )


decodeDict = {
    readchar.key.UP: "UP",
    readchar.key.DOWN: "DOWN",
    readchar.key.ENTER: "ENTER",
}

item = ""


def tempEnd():
    """This is a temporary ending, please insert this at the end of any unfinished code during testing"""

    waittype("Suddenly, you get a violent nosebleed and fall unconscious. The end.")

    waittype("Also this is just a temporary ending so if you see this then congrats.")

    waittype("ok bye")


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

    createMenu(
        "\n".join(scrolltype.log),
        ["Look for the lights", "Search the drawers", "Follow the man"],
        [lightsThree, searchDrawers, follow],
    )


def lightsTwo(manInsideHouse=False):
    """Looking for lights when the man is inside"""

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

    scrollType("What do you do?")

    createMenu(
        "\n".join(scrolltype.log),
        ["Hide", "Try to find a weapon", "Turn on the lights"],
        [hide, findWeapon, lightsOn],
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

    createMenu(
        "\n".join(scrolltype.log),
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
            "Suddenly, his eyes flash dangerously as he notices the knife in your hand. He withdraws a long knife from his pocket immediately and brings it to your neck. You're petrified in fright as he throws away the flashlight takes your knife from your hand."
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

        options(["Follow the man", "Try and turn on the lights", "Search the wardrobe"])

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

    createMenu(
        "\n".join(scrolltype.log),
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
        ["a water bottle", "nothing", "some batteries", "a sock", "an elastic band"], 3
    )

    waittype(
        "You run over to the dresser and pull it open, finding " + item + " inside."
    )

    inv.add(item)

    waittype("You close the drawer. You hear the man reach the top of the stairs.")

    waittype(
        "You shine the flashlight around the room once more, spotting a wardrobe. Although it could contain useful tools and could be used as a hiding place, you think its risky to walk over there."
    )

    scrollType("What do you do?")

    createMenu(
        "\n".join(scrolltype.log),
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

    scrollType("What do you do?")

    createMenu(
        "\n".join(scrolltype.log),
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

    scrollType("What do you do?")

    createMenu(
        "\n".join(scrolltype.log),
        ["Search the wardrobe", "Follow the man", "Turn on the lights"],
        [searchWardrobe2, follow, lightsThree],
    )


def searchWardrobe2():
    """searching the wardrobe after the man leaves after hide2()"""

    waittype(
        "You hear the man shut the front door slowly behind him as he leaves your house."
    )

    waittype(
        "You peek out the window and see him run away, dissapearing into the shadows."
    )

    waittype("After he leaves, you open the wardrobe doors and look inside.")

    generate(
        ["a small dagger", "a tank of gasoline", "a bandaid", "nothing", "a hairpin",],
        3,
    )

    waittype("You find" + item + " in the wardrobe.")

    inv.add(item)

    options(["Follow the man", "Look for the lights"], follow, lightsThree)


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

    scrollType("What do you do?")

    createMenu(
        "\n".join(scrolltype.log),
        ["Follow the man", "Search the drawers"],
        [follow, searchDrawers],
    )


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

    scrollType("What do you do?")

    createMenu(
        "\n".join(scrolltype.log),
        ["Follow the man", "Search the drawers"],
        [follow, searchDrawers],
    )


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

    createMenu(
        "\n".join(scrolltype.log),
        ["Follow the man", "Look for the lights"],
        [follow, lightsThree],
    )


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

    eval(endOfChapterOne("following man"))


def lightsThree():
    """looking for the lights after you hid from the man"""
    waittype("You rummage around the room, looking for the lights.")

    waittype("*rummage rummage rummage*")

    waittype(
        "You find the light switch and flick it on. You look around the room, surpised at how big it actually is."
    )

    waittype(
        "The wardrobe is open with nothing inside. There is a blanket on your bed, which you decide to take with you. You wrap it around your back like a robe.."
    )

    inv.add("blanket")

    waittype(
        "You open the door to the hallway and walk down the stairs. The house is bare, no decorations or furniture anywhere."
    )

    waittype("You reach the front door. You grasp the doorknob and take a deep breath.")

    waittype("You push open the door and step into the outside.")

    endThing = "not following man"

    eval("endOfChapterOne(not following man)")


def endOfChapterOne(endThing):
    """the end of chapter one"""
    waittype("To be continued in Chapter 2")

    waittype(
        "Thank you for playing Chapter 1 of Pukage. This game is currently in pre-alpha, so there may be bugs."
    )

    from chapter2 import Chapter2intro

    createMenu(
        "\n".join(scrolltype.log),
        ["Continue to chapter 2", "Quit", "Retry", "Quit to main menu", "Show credits"],
        [
            "Chapter2intro(endThing)",
            'sys.exit("You exited the game.")',
            intro,
            startingMenu,
            credits,
        ],
    )


def credits():
    """Shows the credits for pukage"""
    createMenu(
        "   _____              _ _ _       \n  / ____|            | (_) |      \n | |     _ __ ___  __| |_| |_ ___ \n | |    | '__/ _ \/ _` | | __/ __|\n | |____| | |  __/ (_| | | |_\__ \\\n  \_____|_|  \___|\__,_|_|\__|___/ \n\n Developers: \n  1. Jeffrey Zang (age 13, Windows 10) \n  2. Li Feng Yin (age 12, Macbook) \n  3. Daniel Zhang (age 12, Chromebook) \n\nTesters: \n  1. The Devs \n  2. Other people soon",
        ["Back"],
        [startingMenu],
    )


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
                        eval(functions[index])
                    except SyntaxError:
                        exec(functions[index])
                    break
                elif type(functions[index]) == list:
                    for func in functions[index]:
                        if type(functions[index] == str):
                            try:
                                eval(func)
                            except SyntaxError:
                                exec(func)
                            break
                            func()
                else:
                    functions[index]()


def reload():
    """reloads"""
    clearConsole()

    menuItems = originalMenuItems.copy()
    indexVal = menuItems[index]
    pointer = indexVal + " «"

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
        "  _____       _                    \n |  __ \     | |                   \n | |__) _   _| | ____ _  __ _  ___ \n |  ___| | | | |/ / _` |/ _` |/ _ \\\n | |   | |_| |   | (_| | (_| |  __/\n |_|    \__,_|_|\_\__,_|\__, |\___|\n                         __/ |     \n                        |___/      ",
        ["Start game", "Settings", "Credits", "Exit game"],
        [intro, settings, credits, 'sys.exit("You exited the game.")'],
        "v1.0.0-alpha",
    )


def generate(choices: List[Any], numberOfChoices):
    """Generates items"""
    tempChoices = choices.copy()
    randomChoices = []
    menuItemsList = []
    menuItemsFunctions = []
    global item
    item = ""

    for i in range(1, numberOfChoices):
        int = randint(0, numberOfChoices)
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


# def generate(choices: List[Any]):
#     global item
#     item = choices[randint(0, len(choices) - 1)]
#     return item;


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
                scrolltype.scrollSpeed = userInputInt / 50
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

    createMenu("Coming soon", ["Back"], [settings])


# i don't need that for what i'm doing


def settings():
    createMenu(
        "   _____      _   _   _                 \n  / ____|    | | | | (_)                \n | (___   ___| |_| |_ _ _ __   __ _ ___ \n  \___ \ / _ | __| __| | '_ \ / _` / __|\n  ____) |  __| |_| |_| | | | | (_| \__ \ \n |_____/ \___|\__|\__|_|_| |_|\__, |___/\n                               __/ |    \n                              |___/     ",
        ["Scroll speed", "Wait time", "Difficulty", "\nBack"],
        [setScrollSpeed, setWaitTime, setDifficulty, startingMenu],
        "v1.0.0-beta",
    )


# def pause():
#     timeSleep(1)
#     while True:
#         c = readchar.readchar()
#         if c == "p":

#             threading.Lock().acquire()
#             createMenu("  _____                         _ \n |  __ \                       | |\n | |__) __ _ _   _ ___  ___  __| |\n |  ___/ _` | | | / __|/ _ \/ _` |\n | |  | (_| | |_| \__ |  __| (_| |\n |_|   \__,_|\__,_|___/\___|\__,_|                                  ", ["Resume Game", "Options", "Quit to title", "Quit"], ["threading.Lock().release()", settings, startingMenu, "sys.exit('You left the game.')"])

# paws = threading.Thread(target=pause)
# paws.start()
# mainThread = threading.main_thread()
if __name__ == "__main__":
    startingMenu()
