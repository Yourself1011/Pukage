from scrolltype import scrolltype
from time import sleep

def waittype(string):
  scrolltype(string)
  time = len(string.split()) * 0.4
  scrolltype('\n\n\n\n')
  sleep(time)