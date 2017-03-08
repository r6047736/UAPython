#
#Author: Javier Saldana
#Description: the script below acts as an interactive program and answers you
#   when you ask a question. after 10 questions the program says goodbye and exits.

import sys

from datetime import datetime

count = 1
colorcount = 1
print('PUTER: Hello and Welcome! Ask me no more than 10 questions.') #initial question

while (count < 11):
    print('PUTER: Go ahead, ask me something:')
    user_input = sys.stdin.readline().rstrip()
    if user_input == "how are you?":
        print ('PUTER: I am a computer program, so obviously I am excellent!')
    elif user_input == "how goes it?":
        print ('PUTER: I am a computer program, so obviously I am excellent!')
    elif user_input == "what is your birthday?":
        print ('PUTER: I am a computer program! I don\'t have a birthday :-(')
    elif user_input == "what is your favorite color?":
        if (colorcount == 1 or colorcount == 4 or colorcount == 7 or colorcount == 10):
            print ('PUTER: red!')
        if (colorcount == 2 or colorcount == 5 or colorcount == 8):
            print ('PUTER: blue!')
        if (colorcount == 3 or colorcount == 6 or colorcount == 9):
            print ('PUTER: green!')
    elif user_input == "what time is it?":
        print ('PUTER:' + str(datetime.now()) )
    elif user_input == "what is the date?":
        print ('PUTER: The current date/time is ' + str(datetime.now()) )
    elif user_input == "exit":
        print ('PUTER: Bye!')
        sys.exit()
    else:
        print ('PUTER: Sorry, I can\'t understand you!')
    count = count + 1
    colorcount = colorcount + 1
print ('PUTER: Question limit reached. Bye!')
sys.exit()
