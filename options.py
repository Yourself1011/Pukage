from time import sleep
from scrolltype import scrolltype
from waittype import waittype



def options(choices, callbackfn1 = 'undefined', callbackfn2 = 'undefined', callbackfn3 = 'undefined', callbackfn4 = 'undefined'):

  scrolltype("What do you do?\n")
  sleep(1)
  for index, item in enumerate(choices):
    scrolltype(str(index + 1) + ': ' + choices[index] + '\n')
    sleep(1)
  scrolltype("Type which option you'd like to choose: \n\n")
  userInput = input()
  choice = userInput.strip()
  
  def tryPrint(function):
    if function == 'undefined':
      newChoice = input("\nThat's not a valid option! Please type 1 or 2: ")
      checkChoice(newChoice)
    else:
      waittype('')
      function()

  def checkChoice(choice):
    if choice != '1' and choice != '2':
      choice = input("That's not a valid option! Please type 1 or 2. ")
      checkChoice(choice)
    elif choice == '1':
        tryPrint(callbackfn1)
    elif choice == '2':
        tryPrint(callbackfn2)
    elif choice == '3':
        tryPrint(callbackfn3)
    elif choice == '4':
        tryPrint(callbackfn4)

  checkChoice(choice)