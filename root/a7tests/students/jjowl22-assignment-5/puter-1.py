#
# Author: Josh Owl
# Description:
# This script is interactive and will print answers to basic questions that are entered.

import sys
from datetime import datetime

print('PUTER: Hello and welcome! Ask me no more than 10 questions')
print('PUTER: Go ahead, ask me something:')


question = 1
count = 2

while question <= 10:
    input = sys.stdin.readline().rstrip()
    if input == 'how goes it?':
        question = question + 1
        print('I am a computer program, so obviously I am excellent!')
        print('PUTER: Go ahead, ask me something:')
    elif input == 'how are you?':
        question = question + 1
        print('I am a computer program, so obviously I am excellent!')
        print('PUTER: Go ahead, ask me something:')
    elif input == 'what is your birthday?':
        question = question + 1
        print("I am a computer program! I don't have a birthday :-(")
        print('PUTER: Go ahead, ask me something:')
    elif input == 'what is your favorite color?':
        question = question + 1
        count = count + 1
        if count % 3 == 0:
            print("red!")
            print('PUTER: Go ahead, ask me something:')
        elif count % 3 == 1:
            print("blue!")
            print('PUTER: Go ahead, ask me something:')
        elif count % 3 == 2:
            print("green!")
            print('PUTER: Go ahead, ask me something:')
    elif input == 'what time is it?':
        question = question + 1
        print("The current date/time is " + str(datetime.now()))
        print('PUTER: Go ahead, ask me something:')
    elif input == 'what is the date?':
        question = question + 1
        print("The current date/time is " + str(datetime.now()))
        print('PUTER: Go ahead, ask me something:')
    elif input == 'exit':
        print("Bye!")
        sys.exit()
    else:
        question = question + 1
        print("Sorry, I can't understand you!")
        print('PUTER: Go ahead, ask me something:')
print("Question limit reached. Bye!")
sys.exit()
