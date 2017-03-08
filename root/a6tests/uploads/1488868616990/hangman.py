#
# Author: Ruby Abrams
# Description:
#    Coding up the Hangman game!
#

import sys

print("GAME: Welcome to HANGMAN!")
print("GAME: player 1 Enter a hangman word:")
hidden_text = sys.stdin.readline().rstrip().lower()

num_guesses = 0
num_errors = 0
complete = False
progress = '_'*len(hidden_text)
guesses = ''
hangman = ""
while not complete:
	print("GAME: Current hangman status:")
	# here I will print the hangman himself
	# Full body
	line1 = "  _"			# head
	line2 = " |_|"			# head
	line3 = "--|--"
	line4 = "  |"
	line5 = " / \ "
	print(hangman)
	print(progress)

	# ask player two to make a guess
	print("GAME: player 2 guess a letter:")
	guess = sys.stdin.readline().rstrip().lower()

	# add the guess to guesses to keep track of guesses made
	guesses+=guess

	if guess in hidden_text:
		print("GAME: YES!")
		# update the progress
		progress  = ''
		for letter in hidden_text:
			if letter in guesses:
				progress += letter
			else:
				progress += '_'
		if progress == hidden_text:
			print("GAME: Current hangman status:")
			print(hangman)
			print(progress)
			print("GAME: player 2 wins!")
			complete = True
	else:
		# update status
		print("GAME: NOPE!")
		num_errors+=1
		if num_errors == 1:
			hangman+=line1+'\n'+line2+'\n'
		elif num_errors == 2:
			hangman+="  |\n  |\n"
		elif num_errors == 3:
			hangman = hangman.replace("\n  |\n  |\n","\n--|\n  |\n")
		elif num_errors == 4:
			hangman = hangman.replace("\n--|\n  |\n","\n--|--\n  |\n")
		elif num_errors == 5:
			hangman+=" / \n"
		else:
			hangman = hangman.replace(" / \n", " / \ \n")
			complete = True
			print("GAME: Current hangman status:")
			print(hangman)
			print(progress)
			print("GAME: player 1 wins!")

	num_guesses += 1
