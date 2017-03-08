#
# Author: Luc Zbonack
# Description:
#    This is a simple version of a question/answer AI. It takes question in through standard input and prints out answers
#    through standard output. The AI will exit after 10 questions or it will exit when the user tells it to. At this time the
#    AI only responds to certain inputs.
# 

import sys
from datetime import datetime

print ("PUTER: Hello and welcome! Ask me no more than 10 questions.")

# Declare counters for total questions and to keep track of color preference
questions = 1
color_count = 0

# Use while loop to track number of questions asked
while (questions <= 10):
    print ("PUTER: Go ahead, ask me something:")
    user_input = sys.stdin.readline().rstrip()
    if (user_input == "how are you?" or user_input == "how goes it?"):
        print ("PUTER: I am a computer program, so obviously I am excellent!")
    
    elif (user_input == "what is your birthday?"):
        print ("PUTER: I am a computer program! I don't have a birthday :-(")
    
    elif (user_input == "what is your favorite color?"):
        if (color_count % 3 == 0):
            print("PUTER: red!")
            color_count += 1
        elif (color_count % 3 == 1):
            print("PUTER: blue!")
            color_count += 1
        elif (color_count % 3 == 2):
            print("PUTER: green!")
            color_count += 1
            
    elif (user_input == "what time is it?" or user_input == "what is the date?"):
        print("PUTER: The current date/time is " + str(datetime.now()))

    elif (user_input == "exit"):
        print ("PUTER: Bye!")
        sys.exit()
        
    else:
        print("PUTER: Sorry, I can't understand you!")
    
    questions +=1

print ("PUTER: Question limit reached. Bye!")
sys.exit()
  
