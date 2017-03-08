#
# Author: Bryce Wakefield
# Description:
#		A AI conversation with the user. 'PUTER' is the AI used similar to Siri, Echo, Etc. It will great the user and instruct them to ask a question
#		The AI will read the question and answer accordingly. When the users asks 10 questions ( valid questions or not) it will print that the limit was reached
# 	 	If the user types 'exit' program will say bye and end. 

import sys

from datetime import datetime

# AI NAME
name = 'PUTER: '
# Statement when question limit reached
limit = 'Question limit reached. Bye!'
# Statement when user types exit
bye = 'Bye!'
# Statement when response is printed and asks for next question
nextquestion = 'Go ahead, ask me something:'
# Statement to check if user wants to quit
exit = 'exit'
# Definition of responses to the questions
responses = {'R1': 'I am a computer program, so obviously I am excellent!', 'R2': 'I am a computer program! I don\'t have a birthday :-(' , 'R4': 'The current date/time is '}
# List of colors to print in order
colors = ('red!', 'blue!', 'green!')
# Questions to check for
q1 = ('how are you?', 'how goes it?')
q2 = 'what is your birthday?'
q3 = 'what is your favorite color?'
q4 = ('what time is it?', 'what is the date?')
# PUTER(AI) Greeting
print(str(name) + "Hello and welcome! Ask me no more than 10 questions.")


# c is used to count which color to print in order
c = 0
# i is the counter to know when limit of 10 questions is reached
i = 1
# while loop to iterate through questions
while i <= 10:
	# Asks for question
	print(str(name) + "Go ahead, ask me something:")
	# Stores users question into variable question 1
	question1 = sys.stdin.readline().rstrip()
	# Checks if user asked how are you? or how goes it and responds
	if question1 == q1[0]:
	 	print(str(name) + str(responses['R1']))	
	 	i += 1
	# Checks if user asked how are you? or how goes it and responds
	elif question1 == q1[1]:
		print(str(name) + str(responses['R1']))	
		i += 1
	# Checks if user asked what is your birthday? and responds
	elif question1 == q2:
		print(str(name) + str(responses['R2']))
		i += 1
	# Checks if user asked what is your favorite color? and responds
	elif question1 == q3:
		print(str(name) + str(colors[c]))
		c += 1
		i += 1
		# if c == 3 then restart the color order
		if c == 3:
			c = 0
	# Checks if user asked what time is it? or what is the date? and responds			
	elif question1 == q4[0]:
		#elif
		print(str(name) + str(responses['R4']) + str(datetime.now()))
		i += 1
	elif question1 == q4[1]:
		#elif
		print(str(name) + str(responses['R4']) + str(datetime.now()))
		i += 1
	# Checks if user types exit if so than exits the program
	elif question1 == exit:
		print(str(name) + bye)
		sys.exit()
	# If none of the questions are valid prints 
	else:
		print("Sorry, I can't understand you!")
		i += 1
# when question limit reaches 10 prints
print(limit)
