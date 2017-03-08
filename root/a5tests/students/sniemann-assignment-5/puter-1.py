#
# Author: Sean Niemann
# Description:
#    Launches an incredibly powerful and intelligent AI system that can answer billions of different questions.
#    ...actually, it's not very intelligent at all.
#

from datetime import datetime

command = ""
question_num = 0
color_index = 0

print("PUTER: Hello and welcome! Ask me no more than 10 questions.")

while True:
    command = input("PUTER: Go ahead, ask me something:\n")
    
    if command == "how are you?" or command == "how goes it":
        print("PUTER: I am a computer program, so obviously I am excellent!")
    elif command == "what is your birthday?":
        print("PUTER: I am a computer program! I don't have a birthday :-(")
    elif command == "what is your favorite color?":
        if color_index % 3 == 0:
            print("PUTER: red!")
        elif color_index % 3 == 1:
            print("PUTER: blue!")
        else:
            print("PUTER: green!")
        color_index += 1
    elif command == "what time is it?" or command == "what is the date?":
        print("PUTER: The current date/time is " + str(datetime.now()))
    elif command == "exit":
        print("PUTER: Bye!")
        break
    else:
        print("PUTER: Sorry, I can't understand you!")
    
    question_num += 1

    if question_num >= 10:
        print("PUTER: Question limit reached. Bye!")
        break