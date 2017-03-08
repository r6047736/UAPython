import sys
from datetime import datetime
color_count = 0
print("PUTER: Hello and welcome! Ask me no more than 10 questions.")
for i in list(range(1,11)):
	print("PUTER: Go ahead, ask me something: ")
	question = sys.stdin.readline().rstrip();
	if question == "how are you?" or question == "how goes it?":
		print("PUTER: I am a computer program, so obviously I am excellent!")
	elif question == "what is your birthday?":
		print("PUTER: I am a computer program! I don't have a birthday :-(")
	elif question == "what is your favorite color?":
		if color_count % 3 == 0:
			print("PUTER: red!")
		if color_count % 3 == 1:
			print("PUTER: blue!")
		if color_count % 3 == 2:
			print("PUTER: green!")
		color_count = color_count + 1
	elif question == "what is the date?" or question == "what time is it?":
		print("PUTER: The current date/time is " + str(datetime.now()))
	elif question == "exit":
		print("PUTER: Bye!")
		sys.exit()
	else:
		print("PUTER: Sorry, I can't understand you!")

print("PUTER: Question limit reached. Bye!")
sys.exit()
