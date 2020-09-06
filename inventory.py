"""
Pukage
Choose-your-own-adventure game.
https://github.com/Yourself1011/Pukage/

Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin, and all Pukage contributors https://github.com/Yourself1011/Pukage/graphs/contributors/

MIT License
"""

from scrolltype import scrolltype
from time import sleep
from waittype import waittype
from items import itemsLibrary
from typing import List, Any, Dict

items = {
  "nothing": None
}

for category in itemsLibrary.keys():
  if category == "nothing":
    continue
  else:
    for item in itemsLibrary[category].values():
      item["category"] = category
      items[item["name"]] = item
      
def removeArticles(word):
    splitWord = list(word)

    if word.startswith("a "):
        splitWord = splitWord[slice(2, len(word))]
    elif word.startswith("an "):
        splitWord = splitWord[slice(3, len(word))]
    elif word.startswith("some "):
        splitWord = splitWord[slice(5, len(word))]
    elif word.startswith("the "):
        splitWord = splitWord[slice(4, len(word))]
    return "".join(splitWord)


class invClass:
    def __init__(self, hands: List[Any] = [], pockets: List[Any] = []):
        def func(invType):
            for item in invType:
              for category in items:
                  if category[removeArticles(item)]:
                      return removeArticles(item)

        try:
          self.hands = list(map(func, hands))
        except TypeError:
          pass

        try:
          self.pockets = list(map(func, pockets))
        except TypeError:
          pass

    def add(self, item):
        from main import createMenu, scrollMenu

        obj = removeArticles(item)

        try:
            obj = items[obj]
        except KeyError:
            print("Oops, that item is not inside items. Go add it now.")

    def remove(self, item):
        obj = removeArticles(item)

        try:
            obj = items[obj]
        except KeyError:
            return print("Oops, that item is not inside items. Go add it now.")

        if obj.size == "big":
            try:
                self.hands.pop(self.hands.index())
                return True
            except ValueError:
                return False

    def has(self, item):
        obj = removeArticles(item)

        try:
            obj = items[obj]
        except KeyError:
            return print("Oops, that item is not inside items. Go add it now.")

        joinedInventory = self.hands + self.pockets

        try:
            joinedInventory.index(item)
            return True
        except ValueError:
            return False

    def show(self):
        def showItems(invType):
            if len(invType) == 0:
                return "n/a"
            return ", ".join(list(map(lambda item: item["name"].capitalize(), invType)))

        return f"Hands: {showItems(self.hands)}\nPockets: {showItems(self.pockets)}"

    hands = []
    pockets = []


inv = invClass(["bandage"])