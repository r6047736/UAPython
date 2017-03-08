#
# Author: Marshal Powell
# Description:
#       In this program, the user will eseentialy have a conversation with the
#   computer.  The user will be able to ask the computer 10 questions.  The
#   computer only recognizes certain questions, however, and will say it
#   cannot understand if the question is not recognized.  After the 10 questions
#   the computer will have a goodbye promt.
#


from datetime import datetime
import sys 

def puter_1():
    questionsAsked = 0
    color = 0
    print("PUTER: Hello and welcome! Ask me no more than 10 questions.")
    
    while questionsAsked < 10:
        print("PUTER: Go ahead, ask me something: ")
        user_input = sys.stdin.readline().rstrip()
        if (user_input == "how are you?" or user_input == "how goes it?"):
            print("PUTER: I'm always good because I am a computer!")
            questionsAsked += 1
        elif (user_input == "what is your birthday?"):
            print("PUTER: I am a computer program! I don't have a birthday :-(")
            questionsAsked += 1
        elif (user_input == "what is your favorite color?"):
            if color == 0 or color == 3 or color == 6 or color == 9:
                print("PUTER: red!")
                color += 1
            elif color == 1 or color == 4 or color == 7 or color == 10:
                print("PUTER: blue!")
                color += 1
            elif color ==2 or color == 5 or color == 8 :
                print("PUTER: green!")
                color += 1
            questionsAsked += 1
        elif user_input == "what time is it?":
            now = datetime.now()
            print("PUTER: " + str(now))
            questionsAsked += 1
        elif user_input == "exit":
            print("PUTER: Bye!")
            sys.exit()
        else :
            print("PUTER: Sorry, I can't understand you!")
            questionsAsked+= 1
    else :
        print("PUTER: Question limit reached. Bye!")
        
            
        


puter_1()
