# Author: Chentao Wang
# Description: return different answers to fixed questions by using while loop
# and if statements
# import sys and datetime to use functions like exit and datetime.now
import sys
from datetime import datetime

print('PUTER: Hello and welcome! Ask me no more than 10 questions.')
# count indicates the question numbers. cnt indicates the number of colors
# in cnt, 1 means red, 2 means blue, 3 means green
count = 0
cnt = 1
# use while loop to exit once question reaches 10
while count <= 10:
    print('PUTER: Go ahead, ask me something:')
    count = count + 1
    # user_input is the varible which is the input we type in
    user_input = sys.stdin.readline().rstrip()
    if user_input == "how are you?" or user_input == "how goes it?":
        print('PUTER: I am a computer program, so obviously I am excellent!')
    elif user_input == "what is your birthday?":
        print("PUTER: I am a computer program! I don't have a birthday :-(")
    elif user_input == "what is your favorite color?":
        if cnt == 1:
            print("PUTER: red!")
        if cnt == 2:
            print("PUTER: blue!")
        if cnt == 3:
            print("PUTER: green!")
        cnt = cnt + 1
        if cnt > 3:
            cnt = 1
    # use str so that datetime won't have error output
    elif user_input == "what time is it?" or user_input == "what is the date?":
        print("PUTER: The current date/time is " + str(datetime.now()))
    elif user_input == "exit":
        print("PUTER: Bye!")
        exit()
    else:
        print("PUTER: Sorry, I can't understand you!")
    if count == 10:
        print("PUTER: Question limit reached. Bye!")
        exit()
