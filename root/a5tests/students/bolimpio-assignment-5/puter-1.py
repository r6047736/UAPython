# Author: Ben Olimpio
# Description:
#   This python program acts as a basic AI where the user can interact
#   with an artificial intelligence bot named Puter. There will be a series
#   of questions that Puter can handle, and the limit of questions that the
#   bot will be able to take is 10.

import sys
from datetime import datetime

print("PUTER: Hello and welcome! Ask me no more than 10 questions.")
print("PUTER: Go ahead, ask me something:")

count = 0
color = "red"

while True:
    if count == 10:
        break
    
    question = sys.stdin.readline().rstrip()
    
    if (question == "how are you?") | (question == "how goes it?"):
        print("PUTER: I am a computer program, so obviously I am excellent!")
        if count < 9:
            print("PUTER: Go ahead, ask me something:")
        count += 1
    elif question == "what is your birthday?":
        print("PUTER: I am a computer program! I don't have a birthday :-(")
        if count < 9:
            print("PUTER: Go ahead, ask me something:")
        count += 1
    elif question == "what is your favorite color?":
        if color == "red":
            print("PUTER: " + color + "!")
            color = "blue"
        elif color == "blue":
            print("PUTER: " + color + "!")
            color = "green"
        elif color == "green":
            print("PUTER: " + color + "!")
            color = "red"
        if count < 9:
            print("PUTER: Go ahead, ask me something:")
        count += 1
    elif (question == "what time is it?") | (question == "what is the date?"):
        print("PUTER: The current date/time is " + str(datetime.now()))
        if count < 9:
            print("PUTER: Go ahead, ask me something:")
        count += 1
    elif question == "exit":
        print("PUTER: Bye!")
        sys.exit()
    else:
        print("PUTER: Sorry, I can't understand you!")
        if count < 9:
            print("PUTER: Go ahead, ask me something:")
        count += 1

print("PUTER: Question limit reached. Bye!")
sys.exit()
    
