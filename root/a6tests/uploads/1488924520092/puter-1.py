'''
Created on Feb 24, 2017

@author: Robert Schweitzer
    Description:
        This script runs as a basic AI that can respond to basic questions.
'''
import sys
from datetime import datetime

color = 0
question = 0

def how_are_you():
    print("PUTER: I am a computer program, so obviously I am excellent!")

def birthday():
    print("PUTER: I am a computer program! I don't have a birthday :-(")
    
def favorite_color():
    global color 
    if color == 0:
        print("PUTER: red!")
        color += 1
    
    elif color == 1:
        print("PUTER: blue!")
        color += 1
    
    else:
        print("PUTER: green!")
        color = 0

def date_time():
    print("PUTER: The current date/time is " + str(datetime.now()))

#Start of the Script
print("PUTER: Hello and welcome! Ask me no more than 10 questions.")

while question < 10:
    
    print("PUTER: Go ahead, ask me something:")
    
    user_input = sys.stdin.readline().rstrip()
    
    if user_input == "how are you?" or user_input == "how goes it?":
        how_are_you()
    
    elif user_input == "what is your birthday?":
        birthday()
    
    elif user_input == "what is your favorite color?":
        favorite_color()
    
    elif user_input == "what time is it?" or user_input == "what is the date?":
        date_time()
        
    elif user_input == "exit":
        print("PUTER: Bye!")
        sys.exit()
    
    else:
        print("Sorry, I can't understand you!")
      
    question += 1

print("PUTER: Question limit reached. Bye!")
