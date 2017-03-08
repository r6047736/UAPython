#
# Author: Kengo Nemoto
# Description:
#    while the "c" variable is below 10, it loops.  And while it
#	 loops, the operator can type in the command and the program
#	 will detect the command by the "if" function.  After answering
#	 one question, the "c" variable will automatically add up by 1.
#	 For the color question, it is designed to add up the "num_color"
#	 variable to answer in a right order.  It will reset to 0 when it
#	 reaches the number 3.

print("PUTER: Hello and welcome! Ask me no more than 10 questions.")
from datetime import datetime
color = ["red", "blue", "green"]
c = 0
num_color = 0
import sys
while c <= 10:
	print("PUTER: Go ahead, ask me something:")
	command = sys.stdin.readline().rstrip()
	if command == "how are you?" or command == "how goes it?":
		print("PUTER: I am a computer program, so obviously I am excellent!")
		c = c + 1
	elif command == 'what is your birthday?':
		print("PUTER: I am a computer program! I don't have a birthday :-(")
		c = c + 1
	elif command == "what is your favorite color?":
			print("PUTER: " + color[num_color] + "!")
			num_color = num_color + 1
			c = c + 1
			if num_color == 3:
				num_color = 0
	elif command == "what time is it?" or command == "what is the date?":
		print("PUTER: The current date/time is " + str(datetime.now()) )
	elif command == "exit":
		print("PUTER: Bye!")	
		sys.exit()
	else:
		print("Sorry, I can't understand you!")
		c = c + 1
	if c == 10:
		print("PUTER: Question limit reached. Bye!")
		sys.exit()


