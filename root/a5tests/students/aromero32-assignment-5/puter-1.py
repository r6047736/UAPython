import sys
from datetime import datetime	
#
# Author: Alex Romero
# Description:
#    This program takes user input and 
#    prints somthing out based on that input.
#    This is done by a while loop, if/else statements
#    as well as by using a counter to count how many questions
#    have been asked

num_question = 10
color_asked = 0 #the number of times the favorite color has been asked
print("PUTER: Hello and welcome! Ask me no more than 10 questions.")

while (True):
	if(num_question == 0):
		print("PUTER: Question limit reached. Bye!")
		sys.exit()
	print("PUTER: Go ahead, ask me something:")
	user_input = sys.stdin.readline().rstrip()
	if(user_input == "exit"):
		print("PUTER: Bye!")
		sys.exit()
	elif(user_input == "how are you?" or user_input == "how goes it?"):
		print("PUTER: I am a computer program, so obviously I am excellent!")
	elif(user_input == "what is your birthday?"):
		print("PUTER: I am a computer program! I don't have a birthday :-(")
	elif(user_input == "what is your favorite color?"):
		if(color_asked == 0):
			print("PUTER: red!")
			color_asked+=1
		elif(color_asked == 1):
			print("PUTER: blue!")
			color_asked+=1
		elif(color_asked == 2):
			print("PUTER: green!")
			color_asked = 0
	elif(user_input == "what time is it?" or user_input == "what is the date?"):
		print("PUTER: The current date/time is", datetime.now())
	else:
		print("PUTER: Sorry, I can't understand you!")
	num_question -= 1
				
