from random import randint
from time import sleep
from scrolltype import scrolltype
from options import options
from waittype import waittype



def intro():
  """Does the intro"""
  sleep(2)
  scrolltype("...", time=0.5)
  sleep(1)

  waittype("Your eyes peek open slowly after a long, deep sleep.")

  waittype("Your room is cold, and dark, and your thin blankets provide minimal warmth.")

  waittype("You rummage around for the lights when suddenly, you hear something outside.")
  
  options(['Investigate', 'Look for the lights'], investigate, lights)



def investigate():
  """investigate option"""
  sleep(2)

  waittype("You feel your way to the window, opening it and peering outside. The night is calm and dark. Only the moonlight shines on the bare sidewalk."
  )
  waittype("Suddenly, you see a black figure emerge from the shadows.")
  waittype("He starts to walk towards your house.")

  options(['Watch the man', 'Look for the lights'], watch, lights)



def lights():
  """Looking for lights"""

  waittype("You look for the lights.")

  waittype("*rummage rummage rummage*")

  scrolltype("...", time=0.5)
  sleep(5)

  waittype("You find the light switch, only to realize that after flicking it on, you are still surrounded in darkness.")

  waittype("Before you could register your shock, you hear a quiet clicking noise immediately followed by a creak as the front door opens and a dark, masked figure steps into your house.")

  options(["Look for a flashlight", "Hide", "Talk to the man"], flashlight, hide, talk)



def watch():
  """Watching the man"""
  waittype(
    "The hooded figure walks slowly and silently toward your house. He leans against the wall and sinks into the shadows."
  )

  waittype(
      "You hear him quietly rummaging in his bag and pulling something out."
  )

  waittype(
    "There is a small click as the front door is unlocked. It creaks as it opens, and then the weird man disappears into it."
  )

  options([
      "Hide", "Look for the lights", "Try and find a weapon"], hide, lightsTwo, findWeapon)
  # + findWeapon())



def hide():
  """Hiding from the man"""

  waittype(
    "You feel around the darkness, trying to find a hiding place. You hear the man slowly walking down the hallway towards the stairs."
  )

  waittype("You bump into the edge of the bed, pain shooting up and down your shoulder. You hear the steps creaking as the man slowly walks up the stairs."
  )
  
  waittype("The man suddenly stops. Seeing your chance, you dive under your bed and lay still."
  )

  hideUnderBed()

  

def lightsTwo():
  """Looking for lights when the man is inside"""

  scrolltype("...", time=0.5)

  waittype("Your heartbeat quickens while you desperately rummage around in search of the lights. You hear the man's footsteps travelling towards the bottom of the stairs.")

  waittype("*rummage rummage rummage*")

  waittype("You finally find the lights, but you already hear the man climbing up the stairs, steps creaking as he draws closer and closer towards your room. You're sure that he will notice if the lights turn on.")

  options(['Hide', 'Try and find a weapon'], hide, findWeapon)

def flashlight():
  waittype("You hear the man walk down the hallway towards the stairs. Your heartbeat quickens as you stumble towards the window.")

  findWeapon()

def findWeapon():

  waittype("You open the windows as wide as you can, letting the moonlight fill up the room. You see a dresser next to bed. You yank open the drawer and find a flashlight."
  )

  waittype("You hear the man start to walk up the stairs. The steps creak as he walks closer and closer to the top of the stairs.")

  options(['Grab the flashlight', 'Keep Searching'], [continueWithFlashlight, keepSearching])



def hideUnderBed():

  waittype("The doorknob jiggles before the man opens the door. He checks his surrondings before he steps inside your room.")

  waittype("He takes a flashlight out of his bag and shines it around the room. You see a thin rifle slung over his back and a knife in his pocket.")

  waittype("He rummages around in your drawers. Your heart is punding furiously in your ribs as you try to keep your breathing quiet.")

  waittype("The man closes the door quietly as he finally exits the room.")

  options(['Follow the man', 'Look for the lights', 'Search the drawers'], [follow, look, findWeapon])


def continueWithFlashlight():

  waittype("You grab the flashlight and quickly flick it on. You hear the man continuing up the stairs. ")



def keepSearching():

  waittype("You drop the flashlight back in the drawer. You open the other cabinet but find nothing. You start to get more and more desperate.")

  waittype("You hear the man reach the top of the stairs. You see a shiny silver object under the desk.")

  waittype("You lumber towards the desk. You drop to your knees and pick it up, recognizing that the object you're holding carefully is a sharp knife.")

  waittype("The man is walking down the hallway. He is only a few metres away from your room.")

  options(['Hold the man hostage with your knife', 'Hide quickly'], interrogate, hide)

intro()