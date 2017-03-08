#==============================================================================
#
# Author: Graham Smith
# Assignment 5: Problem 1 - 'Puter 
# Date: 02/24/2017
#
# Description:
#	
#       A program for question/answer interaction between user and AI.  
#   Questions are printed, then the user is expected to answer accordingly
#   and press enter.  There is a limit on the number of questions the user can
#   ask, defined by the question_limit variable.
#
#==============================================================================

import sys
from datetime import datetime

question_limit = 10
print( 'PUTER: Hello and welcome! Ask me no more than ' + str(question_limit) + ' questions!' )

i = 0
color_count = 0

while i < question_limit:
    print( 'PUTER: Go ahead, ask me something:' )
    user_in = sys.stdin.readline().rstrip()
    
    if ( user_in == 'how are you?' or user_in == 'how goes it?' ):
        print( 'PUTER: I am a computer program, so obiously I am excellent!' )

    elif ( user_in == 'what is your birthday?' ):
        print( "PUTER: I am a computer program! I don't have a birthday :-(" )

    elif ( user_in == "what is your favorite color?" ):
        if ( color_count % 3 == 0 ):
            print( "PUTER: red!" )
        elif (color_count % 3 == 1):
            print ( "PUTER: blue!" )
        else:
            print( "PUTER: green!" )
        color_count += 1

    elif ( user_in == "what time is it?" or user_in == "what is the date?" ):
        print( "PUTER: The current date/time is " + str(datetime.now()) )

    elif ( user_in == "exit" ):
        print( "PUTER: Bye!" )
        exit()

    else:
        print( "PUTER: Sorry, I can't understand you!" )

    i += 1

## After leaving the while loop, this is the last message printed, then the 
## program exits
print( "PUTER: Question limit reached. Bye!" )


    
