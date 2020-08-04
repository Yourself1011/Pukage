"""
Pukage
Choose-your-own-adventure game.
Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin
MIT License
"""

from time import sleep as timeSleep
import scrolltype
from waittype import waittype
from settings import gameSettings
import readchar.readchar
import readchar.key
from typing import List, Any
from os import system, name

decodeDict = {
    readchar.key.UP: "UP",
    readchar.key.DOWN: "DOWN",
    readchar.key.ENTER: "ENTER",
}


def sleep(*arg):
    pass
    if gameSettings["fastmode"] != "yes":
        sleep = timeSleep


def options(
    choices,
    callbackfn1="undefined",
    callbackfn2="undefined",
    callbackfn3="undefined",
    callbackfn4="undefined",
):

    scrolltype("What do you do?\n")
    sleep(1)

    for index, item in enumerate(choices):
        scrolltype(str(index + 1) + ": " + choices[index] + "\n")
        sleep(1)
    scrolltype("Type which option you'd like to choose: \n\n")
    userInput = input()
    choice = userInput.strip()

    def tryPrint(function):
        if function == "undefined":
            newChoice = input(
                "\nThat's not a valid option! Please type the number of the option like 1 or 2: "
            )
            checkChoice(newChoice)
        else:
            waittype("")
            sleep(1)
            function()

    def checkChoice(choice):
        if choice == "1":
            tryPrint(callbackfn1)
        elif choice == "2":
            tryPrint(callbackfn2)
        elif choice == "3":
            tryPrint(callbackfn3)
        elif choice == "4":
            tryPrint(callbackfn4)
        else:
            choice = input("That's not a valid option! Please type 1 or 2. ")
            checkChoice(choice)

    checkChoice(choice)


def createChoice(listOfChoices):
    for index, item in enumerate(listOfChoices):
        scrolltype(str(index + 1) + ": " + listOfChoices[index] + "\n")
        sleep(1)
    scrolltype("Type which option you'd like to choose: \n\n")
    userInput = input()

    def checkChoice(choice):
        for index, item in enumerate(listOfChoices, 1):
            if int(choice) == index:
                return index
                break
        choice = input(
            "That's not a valid option! Please type the number of the choice you want like 1 or 2."
        )
        checkChoice(choice)

    checkChoice(userInput.strip())


def genRandomItem(items):
    createChoice()


def createMenu(
    headertext,
    menuitems: List[Any],
    functions: List[Any],
    footertext: str = "",
    clear: bool = True,
):

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

            elif "{}".format(decodeDict[c]) == "DOWN":
                if index != int(len(menuItems) - 1):
                    index += 1
                    reload()

            elif "{}".format(decodeDict[c]) == "ENTER":
                if clear:
                    clearConsole()
                    scrolltype.log = []
                try:
                    if type(functions[index]) == list:
                        for func in functions[index]:
                            eval(func)
                    else:
                        eval(functions[index])
                except SyntaxError:
                    if type(functions[index]) == list:
                        for func in functions[index]:
                            exec(func)
                    else:
                        exec(functions[index])
                break


def reload():

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
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
