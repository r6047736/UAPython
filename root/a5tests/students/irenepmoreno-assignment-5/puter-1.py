# Author: Irene Moreno
# Description: this script runs a simple AI named "Puter"

import sys
from datetime import datetime

print("Puter: Hello and welcome! Ask me no more than 10 questions.")
i = 0
j = 0
while i < 10:
    print("PUTER: Go ahead, ask me something:")
    user_input = sys.stdin.readline().rstrip()
    if (user_input == "how are you?" or user_input == "how goes it?"):
        print("PUTER: I am a computer program, so obviously I am excellent!")
    elif (user_input == "what is your birthday?"):
        print("PUTER: I am a computer program! I don't have a birthday :-(")
    elif (user_input == "what is your favorite color?"):
        if (j%3 == 0):
            print("PUTER: red!")
        if (j%3 == 1):
            print("PUTER: blue!")
        if (j%3 == 2):
            print("PUTER: green!")
        j = j + 1
    elif (user_input == "what time is it?" or user_input == "what is the date?"):
        print("The current date/time is " + str(datetime.now()))
    elif (user_input == "exit"):
        print("PUTER: Bye!")
        sys.exit()
    else:
        print("PUTER: Sorry, I can't understand you!")
    i = i + 1
print("PUTER: Question limit reached. Bye!")
sys.exit()
