from scrolltype import scrolltype
from time import sleep


waitTime = 0.5

def waittype(string):
    scrolltype(string);
    time = len(string.split()) * waitTime
    scrolltype("\n\n\n\n")
    sleep(time)


# waittype scrolltypes, then calculates the amount of words, then waits for that amount, then generates new lines(\n\n\n\n)
