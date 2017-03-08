#
# Author: Austin Mutschler
# Description:
#    "The smartest AI you have ever seen, believe me." -Donald Trump
#
import sys

color_count = 0
question_count = 0

print("PUTER: Hello and welcome! Ask me no more than 10 questions.")
while(True):
    if(question_count >= 10):
        print("PUTER: Question limit reached. Bye!")
        sys.exit()
    else:
        print("PUTER: Go ahead, ask me something:")
        user_response = sys.stdin.readline().rstrip()
        question_count += 1

        if(user_response.lower() == "exit"):
            print("PUTER: Bye!")
            sys.exit()

        elif(user_response.lower() == "how are you?" or user_response.lower() == "how goes it?"):
            print("PUTER: I am a computer program, so obviously I am excellent!")

        elif(user_response.lower() == "what is your birthday?"):
            print("PUTER: I am a computer program! I don't have a birthday :-(")

        elif(user_response.lower() == "what is your favorite color?"):
            if(color_count == 0):
                color = "red"
                color_count += 1
                print("PUTER: " + color + "!")

            elif(color_count == 1):
                color = "blue"
                color_count += 1
                print("PUTER: " + color + "!")

            elif(color_count == 2):
                color = "green"
                color_count = 0
                print("PUTER: " + color + "!")

        elif(user_response.lower() == "what time is it?" or user_response.lower() == "what is the date?"):
            import datetime
            print("The current date/time is %s" % datetime.datetime.now())

        else:
            print("PUTER: Sorry, I can't understand you!")
