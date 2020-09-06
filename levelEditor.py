"""
Pukage
Choose-your-own-adventure game.
https://github.com/Yourself1011/Pukage/

Copyright 2020 Daniel Zhang, Jeffrey Zang, Li Feng Yin, and all Pukage contributors https://github.com/Yourself1011/Pukage/graphs/contributors/

MIT License
"""

import pymongo
import os
from waittype import waittype as waitType
from time import sleep
from bson.objectid import ObjectId

uri = os.getenv('MONGOCLIENT')

mongoClient = pymongo.MongoClient(uri)

userDB = mongoClient.users

userColl = userDB.users

levels = mongoClient.levels.levels

user = None


def levelsMenu():
    from main import createMenu

    createMenu(
        """   _____          _                    _                _     
  / ____|        | |                  | |              | |    
 | |    _   _ ___| |_ ___  _ __ ___   | | _____   _____| |___ 
 | |   | | | / __| __/ _ \| '_ ` _ \  | |/ _ \ \ / / _ | / __|
 | |___| |_| \__ | || (_) | | | | | | | |  __/\ V |  __| \__ \\
  \_____\__,_|___/\__\___/|_| |_| |_| |_|\___| \_/ \___|_|___/""",
        ["Your levels", "Browse levels"],
        [yourLevels],
    )


def yourLevels():
    from main import createMenu

    if not user:
        createMenu(
            """ __     __         
 \ \   / /         
  \ \_/ ___  _   _ 
   \   / _ \| | | |
    | | (_) | |_| |
    |_|\___/ \__,_|""",
            ["Sign in", "Sign up"],
            [signIn, signUp],
        )
    else:
        levelsNames = ["New Level"]
        levelFuncs = [editor]
        for i in user["levels"]:
            levelsNames.append(levels.find_one({"_id": ObjectId(i)})["name"])
            levelFuncs.append("levelEditor.showLevel('" + str(levels.find_one({"_id": ObjectId(i)})["_id"]) + "')")
        print(f"{user['levels']}\n{levelsNames}\n{levelFuncs}")
        sleep(10)
        levelsNames.append("Tutorial")
        levelFuncs.append(tutorial)
        createMenu("""  _                    _     
 | |                  | |    
 | |     _____   _____| |___ 
 | |    / _ \ \ / / _ \ / __|
 | |___|  __/\ V /  __/ \__ \\
 |______\___| \_/ \___|_|___/
        """, levelsNames, levelFuncs)

def showLevel(levelID):
    from main import createMenu
    level = levels.find_one({"_id": ObjectId(levelID)})
    createMenu(level["name"], ["Play", "Edit", "Delete"], ["", "levelEditor.editor('" + levelID + "')", f"levelEditor.delete('{levelID}')"])

def delete(levelID):
    from main import createMenu
    level = levels.find_one({"_id": ObjectId(levelID)})
    createMenu(f"Are you absolutely, positively, 100%, find more words for this at https://www.thesaurus.com/browse/absolutely?s=t sure that you want to delete {level['name']}? It will be gone FOREVER. You will never be able to get it back.", ["Yes, please delete the level already", "\nBack"], [f"levelEditor.actuallyDelete('{levelID}')", yourLevels])

def actuallyDelete(levelID):
    deletedLvl = levels.find_one({"_id": ObjectId(levelID)})
    lvlPos = user["levels"].index(levelID)
    userColl.update_one({"_id": user["_id"]}, {"$pop": {"levels": lvlPos}})
    levels.delete_one({"_id": ObjectId(levelID)})
    waitType(f"You deleted {deletedLvl['name']}")
    yourLevels()

def editor(lvlID = "new"):
    from main import clearConsole
    if lvlID == "new":
        levelID = 0
        levelName = "Untitled level"
        levelLines = []
    else:
        level = levels.find_one({"_id": ObjectId(lvlID)})
        levelID = level["_id"]
        levelName = level["name"]
        levelLines = level["lines"]
    print("If you have no clue what you're doing, type c:exit and read the tutorial")
    while True:
        line = input()
        try:
            if (
                line.startswith("c:")
                or line.startswith("cmd:")
                or line.startswith("command:")
            ):
                argsStr = line.split(":")[1]
                args = argsStr.split(", ")
                if args[0] == "exit":
                    break
                elif args[0] == "save" or args[0] == "s":
                    if not bool(levelID):
                        levelID = str(levels.insert_one(
                            {
                                "name": levelName,
                                "author": user["username"],
                                "lines": levelLines,
                                "reputation": 0
                            }
                        ).inserted_id)
                        userColl.update_one(
                            {"_id": user["_id"]}, {"$push": {"levels": levelID}}
                        )
                    else:
                        levels.update_one(
                            {"_id": levelID}, {"$set":{"name": levelName, "lines": levelLines}}
                        )
                elif args[0] == "edit" or args[0] == "e":
                    lineToEdit = int(args[1]) - 1
                    levelLines.pop(lineToEdit)
                    levelLines.insert(lineToEdit, args[2])
                elif args[0] == "delete" or args[0] == "d":
                    levelLines.pop(int(args[1]) - 1)
                elif args[0] == "title" or args[0] == "t":
                    levelName = args[1]
            else:
                levelLines.append(line)
            linesToShow = []
            for i in range(len(levelLines)):
                linesToShow.append(str(i + 1) + ". " + levelLines[i])
            clearConsole()
            print("\n".join(linesToShow))
        except:
            levelLines.append(line)
            linesToShow = []
            for i in range(len(levelLines)):
                linesToShow.append(str(i + 1) + ". " + levelLines[i])
            clearConsole()
            print("\n".join(linesToShow))
    yourLevels()

def tutorial():
    waitType("Please go to https://d-zhang200788.gitbook.io/pukage/custom-level-editor/.")

    sleep(10)
    yourLevels()

def signIn():
    username = input("Username: ")
    password = input("Password: ")

    if (
        not bool(userColl.find_one({"username": username}))
        or userColl.find_one({"username": username})["password"] != password
    ):
        waitType("Incorrect credentials. If you don't have an account, sign up.")

        yourLevels()

    else:
        global user
        user = userColl.find_one({"username": username})
        yourLevels()


def signUp():
    from main import clearConsole

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if bool(userColl.count_documents({"username": username})):
            clearConsole()
            waitType("That username is already taken!")
        else:
            userColl.insert_one(
                {"username": username, "password": password, "levels": []}
            )
            global user
            user = userColl.find_one({"username": username})
            clearConsole()
            break
    yourLevels()

def play(levelID):
    from main import createMenu
    level = levels.find_one({"_id": levelID})
    global line
    for line in level["lines"]:
        # try:
        if line.startswith("t:") or line.startswith("text:"):
            waitType(line.split(":")[1])
        elif line.startswith("s:") or line.startswith("split:"):
            options = []
            names = []
            start = None
            endForOption = None
            for optionfindint in level["lines"].length:
                optionfind = level["lines"][optionfindint]
                if optionfind.startswith("o:") or optionfind.startswith("option:"):
                    names.append(optionfind.split(":").split(", ")[0])
                    splitNames = optionfind.split(":")[1].split(", ")
                    splitNames.pop(0)
                    for titles in splitNames:
                        if titles == line.split(":")[1]:
                            if not endForOption:
                                start = optionfindint
                                return
                            else:
                                try:
                                    endForOption = optionfindint
                                    options.append(f"levelEditor.line = {start}\nlevelEditor.end = {endForOption}")
                                    start = optionfindint
                                    return
                                except IndexError:
                                    optionfindint
                                    options.append(f"levelEditor.line = {start}")
            createMenu(line.split(":")[1], names, options)
        # except:
        #     waitType(line)
    showLevel(levelID)