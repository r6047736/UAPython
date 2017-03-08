#!/usr/bin/env python

#
# Author: Patrick Wilkening
# Description:
#	a puter program that can answer some basic questions
#	(up to 10 questions) before exiting.
#

import sys
import datetime

qCount = 0
color = 0
manual_exit = False

# Questions PUTER will answer
Q1 = "how are you?"
Q2 = "how goes it?"
Q3 = "what is your birthday?"
Q4 = "what is your favorite color?"
Q5 = "what time is it?"
Q6 = "what is the date?"
# get these questions wrong you are thrown off the bridge of death

print("PUTER: Hello and welcome! Ask me no more than 10 questions.")
print("PUTER: Go ahead, ask me something:")

while qCount < 10:
	user_input = sys.stdin.readline().rstrip()
	if user_input == Q1 or user_input == Q2:
		print("PUTER: I am a computer program, so obviously I am excellent!")
	elif user_input == Q3:
		print("PUTER: I am a computer program! I don't have a birthday :-(")
	elif user_input == Q4:
		if (color % 3) == 0:
			print("PUTER: red!")
		elif (color % 3) == 1:
			print("PUTER: blue!")
		else:
			print("PUTER: green!")
		color += 1
	elif user_input == Q5 or user_input == Q6:
		time = str(datetime.datetime.now())
		print ("PUTER: The current date/time is " + time)
	elif user_input == "exit":
		print ("PUTER: Bye!")
		manual_exit = True
		break
	else:
		print ("PUTER: Sorry, I can't understand you!")
	
	qCount += 1
	if qCount < 10:
		print("PUTER: Go ahead, ask me something:")
	
if not manual_exit:
	print("PUTER: Question limit reached. Bye!")
exit()
