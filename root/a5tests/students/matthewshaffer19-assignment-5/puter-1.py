#
# Author: Matthew Shaffer
# Description:
#   This code is designed to function as a basic AI and answer basic questions.
#

import sys
from datetime import datetime

questionCounter = 0
colorCounter = 0

while questionCounter < 10:
    
    if questionCounter == 0:
        print('PUTER: Hello and welcome! Ask me no more than 10 questions.')
    
    print('PUTER: Go ahead, ask me something: ')
    
    user_input = sys.stdin.readline().rstrip()
    
    if user_input == 'exit':
        questionCounter = 10
        print('PUTER: Bye!')
        sys.exit()
    
    elif user_input == 'how are you?' or user_input == 'how goes it?':
        questionCounter += 1
        print('PUTER: I am a computer program, so obviously I am excellent!')
    
    elif user_input == 'what is your birthday?':
        questionCounter += 1
        print("PUTER: I am a computer program! I don't have a birthday :-(")
    
    elif user_input == 'what is your favorite color?':
        if colorCounter == 0:
            print("PUTER: red!")
            colorCounter += 1
        elif colorCounter == 1:
            print("PUTER: blue!")
            colorCounter += 1
        elif colorCounter == 2:
            print("PUTER: green!")
            colorCounter = 0
        questionCounter += 1
    
    elif user_input == 'what time is it?' or user_input == 'what is the date?':
        print("PUTER: The current date/time is" , datetime.now())
        questionCounter += 1
    
    else:
        print("PUTER: Sorry, I can't understand you!")
        questionCounter += 1
    
    if questionCounter == 10:
        print('PUTER: Question limit reached. Bye!')
        sys.exit()
    