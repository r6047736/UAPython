# Thaddeus Semon
# Assignment 5
# The program is a simplified version of an artificial intelligence
# Due February 24, 2017 at 6:00 PM

from datetime import datetime
import sys

print("Hello and welcome! Ask me no more than 10 questions.")
count = 1
color_count = 1
user_input = ''
while (count <= 10):
#    print(count)
    how_are_you = "how are you?"
    how_goes_it = "how goes it?"
    birthday = "what is your birthday?"
    color = "what is your favorite color?"
    time1 = "what time is it?"
    date1 = "what is the date?"
    end = "exit"
    print("PUTER: Go ahead, ask me something:")
    user_input = sys.stdin.readline().rstrip()
    if (user_input == how_are_you or user_input == how_goes_it):
        print("PUTER: I am a computer program, so obviously I am excellent!")

    if (user_input == "what is your birthday?"):
        print("PUTER: I am a computer program! I don't have a birthday :-(")

    if (user_input == "what is your favorite color?"):
        if (color_count == 1 or color_count == 4 or color_count == 7 or
        color_count == 10):
            print ("red!")
            color_count = color_count + 1
        elif (color_count == 2 or color_count == 5 or color_count == 8):
            print("blue!")
            color_count = color_count + 1
        elif (color_count == 3 or color_count == 6 or color_count == 9):
            print("green!")
            color_count = color_count + 1

    if (user_input == "what time is it?" or user_input == "what is the date?"):
        print("The current date/time is " + str(datetime.now()))

    if (user_input != how_are_you and user_input != how_goes_it and user_input
    != birthday and user_input != color and user_input != time1 and user_input
    != date1 and user_input != end):
        print("PUTER: Sorry, I can't understand you! ")

    if (user_input == "exit"):
        print("PUTER: Bye!")
        count = 11

    if (count == 10):
        print("PUTER: Question limit reached. Bye!")

    count = count + 1
