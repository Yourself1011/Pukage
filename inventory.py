"""
Pukage
Choose-your-own-adventure game.
Copyright 2020 Daniel Zhang, Jeffery Zang, Li Feng Yin
MIT License
"""

from scrolltype import scrolltype
from time import sleep
from waittype import waittype
from items import itemsLibrary


def addItem(item):
    obj = itemsLibrary["removeArticles"](item)

    try:
        obj = itemsLibrary[obj]
    except KeyError:
        return print("Oops, that item is not inside itemsLibrary. Go add it now.")

    def checkChoice(choice):
        if choice == "yes" or choice == "y":
            return "yes"
        elif choice == "no" or choice == "n":
            return "no"
        else:
            userInput = input(
                "\nThat's not a valid option! Please respond with yes or no: "
            )
            checkChoice(userInput.lower().strip())

    def checkChoiceNumbers(choice):
        if choice == "1":
            return "1"
        elif choice == "2":
            return "1"
        elif choice == "3":
            return "3"
        else:
            userInput = input(
                "\nThat's not a valid option! Please respond with 1, 2, or 3"
            )
            checkChoice(userInput.lower().strip())

    def tryReplaceHands(obj):
        scrolltype(
            "\nYou cannot hold two items at once. Would you like to replace "
            + inv.hands.name[0]
            + " with "
            + obj.name
            + ", or keep "
            + inv.hands.name[0]
            + "?"
        )

        print("\n\n")

        scrolltype("Please respond with yes/y or no/n.")

        userInput = input()

        checkChoice(userInput.lower().strip())

    def tryReplacePockets(obj):
        scrolltype(
            "\nYou cannot put three items in your pockets at once. Respond with ...\n1 to replace your "
            + inv.hands.name[0]
            + " with the "
            + obj.name
            + "\n2 to replace your "
            + inv.hands.name[0]
            + "with the "
            + obj.name
            + "\n or 3 to leave the "
            + obj
            + " behind."
        )

        userInput = input()

        checkChoiceNumbers(userInput.lower().strip())

    if obj["size"] == "big":
        if len(inv.hands) >= 1:
            tryReplaceHands()
        else:
            inv.hands.append(obj)
    elif obj["size"] == "nothing":
        return
    else:
        if len(inv.pockets) >= 2:
            if len(inv.hands) >= 1:

                scrolltype(
                    "\nWould you like keep this item in your pockets, hold it in your hands, or leave it behind?"
                )

                print("\n\n")

                scrolltype(
                    "Please respond with 1 to put this object in your pocket, 2 to hold this object in your hands, or 3 to leave it behind."
                )

                userInput = input()
                option = checkChoiceNumbers(userInput.lower().strip())

                if option == "3":
                    return
                elif option == "2":
                    if len(inv.hands) >= 1:
                        tryReplaceHands()
                    else:
                        inv.hands.append(obj)
                elif option == "1":
                    pass
                else:
                    tryReplaceHands()

            else:
                inv.hands.append(obj)
        else:
            inv.pockets.append(obj)


def removeItem(item):
    obj = itemsLibrary["removeArticles"](item)

    try:
        obj = itemsLibrary[obj]
    except KeyError:
        return print("Oops, that item is not inside itemsLibrary. Go add it now.")

    if obj.size == "big":
        try:
            inv.hands.pop(inv.hands.index())
            return True
        except ValueError:
            return False


def checkItem(item):
    obj = itemsLibrary["removeArticles"](item)

    try:
        obj = itemsLibrary[obj]
    except KeyError:
        return print("Oops, that item is not inside itemsLibrary. Go add it now.")

    if obj.size == "nothing":
        return False

    elif obj.size == "big":
        try:
            inv.hands[inv.hands.index(obj)]
        except ValueError:
            return False

        return True

    else:
        try:
            if inv.hands[inv.hands.index(obj)]:
                return "hands"
            elif inv.pockets[inv.pockets.index(obj)]:
                return "pockets"
            else:
                return False
        except ValueError:
            return False


class invClass:
    def add(self, item):
        return addItem(item)

    def remove(self, item):
        return removeItem(item)

    def find(self, item):
        return checkItem(item)

    def has(self, item):
        return checkItem(item) != False

    hands = []
    pockets = []


inv = invClass()

items = itemsLibrary
