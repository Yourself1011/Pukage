# Here is the changelog, where new updates will be posted. #

## Dates ##
- [August 19](#August-19)
- [August 18](#August-18)
-	[August 16](#August-16)
-   [August 12](#August-12)
-   [August 11](#August-11)
-   [August 10](#August-10)
-	[August 3](#August-3)
-	[August 2](#August-2)
-   [August 1](#August-1)
-   [July 31](#July-25)
-   [July 30](#July-24)
-   [July 23](#July-23)
-   [July 22](#July-22)
-   [June 19](#June-19)
-   [June 18](#June-18)
-   [June 17](#June-17)
-   [June 15](#June-15)
-   [June 11](#June-11)
-   [July 7](#July-7)
#   2020

## September 6 ##
- Daniel Zhang - Finished the editor. Prone to many bugs.
- Daniel Zhang - Started letting people play the levels

## August 25 ##
- Jeffrey Zang - Did more work on the story

## August 24 ##
- Jeffrey Zang - Did some work on the story, especially `goDownstairs` and stuff

## August 19 ##
- Li Feng Yin - Modified `waittype` function to accept a list as a parameter and waittype multiple paragraphs

## August 18 ##

- Jeffrey Zang - Made nightmares to scare your balls off in Pukage just like in real life

## August 16 ##

- Jeffrey Zang - Did some work on the story, specifically the part where the man first meets the player
- Jeffrey Zang - Made `healed`, `ate`, and `slept` functions
- Daniel Zhang - Made users and signups/signins

## August 12 ##

- Daniel Zhang - Added a splash of colour to the otherwise bland terminal.
- Jeffrey Zang - Gave up cause he was too stupid
- Daniel Zhang - Corrected the order of the changelog

## August 11 ##

- Li Feng Yin - Moved `createMenu` to new file
- Li Feng Yin - Started rewriting `inv.add`

## August 10 ##

- Li Feng Yin - Fixed problems with circular imports between `main.py` and `chapter2.py`
- Daniel Zhang - Made a fighting engine with his big big big big big big big big brain
- Jeffrey Zang - Made a cow happen
- Daniel Zhang - Actually fixed circular imports
- Daniel Zhang - Added characters.
- Daniel Zhang - Asked Jeffrey what is up with the odd changes.

## August 3 ##
- Daniel Zhang - Made difficulty settings and `scrollMenu()`
- Luke Zhang - fix(CI): fix workflow syntax and steps (#2)
- Luke Zhang - fix: make sure linter is passing #1
- Jeffrey Zang - Changed the waitTime from 0.24 to 0.2 because of popular player preference

## August 2 ##
- Jeffrey Zang - Made way too many functions
	- `tryingToGoIn`
	-	`getIntoTrapdoorWithBoxes`
	- `getIntoTrapdoorWithGenerator`
	- `breakWindow`
	- `enterThroughDoor`
	- `searchBoxes`
	- `exitThroughTrapdoor`
	- `hide5`
	- `pleaseDontHurtMeImJustExploring`
	- `fight`
- Jeffrey Zang - Finished some functions
	- `hide3`
	- `tryingToGoIn`
	- `getIntoTrapdoorWithBoxes`
	- `getIntoTrapdoorWithGenerator`
- Daniel Zhang - Changed the scrollspeed from 0.1 to 0.05 because of popular player preference, and made the setting divide by 100 instead of 50
- Daniel Zhang - Made the stats, hunger, energy, and health
- Daniel Zhang - Made `gotTired`, `gotHungry`, `gotHurt`, and `commitDie` functions

## August 1 ## 
- Jeffrey Zang - Fixed ALL the bugs in Pukage - We can now start doing Chapter 2
- Jeffrey Zang - Add the `jeffInfo`, `danInfo`, and `liFengInfo` functions, which allows the user to see more info about the devs
- Jeffrey Zang - Fixed a couple bugs that I made myself
- Jeffrey Zang - Changed the wait time between lines from 0.5 to 0.3 because of popular player preference
- Daniel Zhang - Began new key reading system
- Daniel Zhang - Cleaned toothpaste off the ceiling

## July 31 ## 
- Jeffrey Zang - Created the `follow3` and `explore` functions
- Jeffrey Zang - Created the `hide3`, `hide4` and `confrontTheMan` functions
- Jeffrey Zang - Created the `lighthouse`, `backToHouse`, `restaurant`, and `bank` functions
- Daniel Zhang - Made GitHub repository, added MIT licence.
- Daniel Zhang - Added `README.md` file
- Jeffrey Zang - Added the difficulty thing
- Somebody who tried to be Li Feng Yin - Made fresh tacos for all of us! <3

## July 30 ##
- Jeffrey Zang - Created the `follow2` function and `Chapter2Intro` functions
- Li Feng Yin - Created the `leavingWithoutFollowingMan` function
- Everyone - Brainstormed ideas for how the rest of Pukage should go

## July 23 ##
- Jeffrey Zang - Created `chapter2.py` file

## July 22 ##
- Jeffrey Zang - Created `endOfChapterOne` function 
- Jeffrey Zang - finished `lightsThree` and `follow`
- Everyone - Finished chapter 1 of Pukage

## July 8 ##
- Daniel Zhang - Created cool awesome perfect fantastic cool functional menu thing
- Daniel Zhang - Fixed Scrolltype bug

## July 7 ##
-   Li Feng Yin - Added a `try...except` to the intro, to control errors
-   Li Feng Yin - Added a `finally` after the `try...except` that executes the `tempEnd` function
- Daniel Zhang - Created "seed" system for determining loot

## June 19 ##
-   Li Feng Yin - Added `fastmode` setting, which disables `sleep()` and `scrolltype()`
-   Li Feng Yin - Fixed the problems with inventory\["add"]
-   Li Feng Yin - Added new `removeArticles` method inside the `items` object that removes articles like "a" and "some" from an item
-   Li Feng Yin - Made the `inv.add()` function easier to use
-   Li Feng Yin - Added the "soodo places" file, used to keep track of the places in the story and what items you can find inside them

## June 18 ##
-   Jeffrey Zang - Added the `tempEnd` function, used at the end of unfinished code during testing
-   Jeffrey Zang - Added the [soodo story](https://repl.it/@LargAnk/pukage#soodo/soodo-story) file, used to keep all the functions in order
-   Jeffrey Zang - Added more story functions: `searchWardrobe2()`, `searchDrawers`, `follow`, `lights3`, `talk`
-   Jeffrey Zang - Finished the `hide2` function
-   Jeffrey Zang - Cleaned up the water spillage from last night
-   Li Feng Yin - Replaced the `lights` option in `investigate()` to `lights2`, a small but crucial change
-   Li Feng Yin - Made and added items to `items.py`

## June 17 ##
-   Jeffrey Zang - Added the `hide2()` function
-   Li Feng Yin - Added the  `stay()` and `searchWardrobe()` functions

## June 15 ##
-   Jeffrey Zang - Changed the `hide()` function, add the `keepSearching()` and `continueWithFlashlight()` functions, added the inv object
-   Li Feng Yin - Added `add()` function

## June 11 ##
-   Li Feng Yin - Made new waittype function that automatically finds the time it takes to read a paragraph then waits for that long. It will also generate new lines `(\n\n\n\n)`.
-   Jeffrey Zang - Extended the `hide()` function
