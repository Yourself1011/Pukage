"""
Pukage
Choose-your-own-adventure game.
Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin
MIT License
"""

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


itemsLibrary = {
    "removeArticles": removeArticles,
    "nothing": {"name": "nothing", "size": "nothing"},
    "flashlight": {"name": "flashlight", "type": ["light"], "size": "small",},
    "bandage": {"name": "bandage", "type": ["heal"], "size": "small",},
    "elastic band": {"name": "elastic band", "size": "small",},
    "water bottle": {"name": "water bottle", "size": "small",},
    "sock": {"name": "sock", "size": "small",},
    "batteries": {"name": "batteries", "type": ["power"], "size": "small",},
    "paperclip": {"name": "paperclip", "size": "small",},
    "small dagger": {"name": "small dagger", "size": "small", "type": ["weapon"],},
    "small knife": {"name": "small knife", "size": "small", "type": ["weapon"],},
    "tank of gasoline": {"name": "tank of gasoline", "size": "big", "type": ["fuel"]},
    "hairpin": {"name": "hairpin", "size": "small"},
    "blanket": {"name": "blanket", "size": "large" }
}
