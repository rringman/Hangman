import random
def choose_word():
	choose_word = ['hackbright', 'coding', 'learn', 'python', 'program']

	chosen_word = (random.choice(choose_word))
	# print chosen_word
	return list (chosen_word)

print "Welcome to Hangman"
def play_hangman():
	user_input = raw_input("Would you like to play? Type Y or N ")
	blank_word=[]
	guesses = []

	if user_input.upper() == "Y": 
		

		chosen_word = choose_word()
		display_function(chosen_word)
		blank_word = list('_'* len(chosen_word))
		begin_guessing(chosen_word, blank_word, guesses)
	else: 
		exit()

def start_game(chosen_word): 
	pass
	
def display_function(chosen_word):
	length = len(chosen_word)
	print "I'm thinking of a word", str(length), "characters long"
	#print length * "_ "

def begin_guessing(chosen_word, blank_word, guesses): 
	while True: 
		printing_guessed_word(blank_word)
		guess = raw_input ("Guess a letter ")
		# print guess
		number_of_guesses(guesses)
		if guess in chosen_word:
			print "Yes!"
			for i in range (len(blank_word)):
				if guess == chosen_word[i]:
					#print blank_word[i],chosen_word[i]
					blank_word[i] = chosen_word[i]
					#print blank_word
			winning(blank_word,chosen_word)		

		else: 
			guesses.append(guess)
			print "Incorrect! You have", 16 - len(guesses), "guesses left!" 
			#print "GUESSES", guesses, len(guesses)
			print "So far you've guessed",
			for letter in guesses:
				print letter,
			print " "

			#for letter in guesses: 
				#print letter,
			#print blank_word

def printing_guessed_word(blank_word):
	for letter in blank_word: 
		print letter + " ",
	print " " 


def number_of_guesses(guesses):
	# print len(guesses)
	if len(guesses) > 15: 
		print ("No more guesses! Your man is hung")
		play_hangman() 

def winning(blank_word,chosen_word):
	#print blank_word, chosen_word
	if blank_word == chosen_word: 
		print "You win!"
		play_hangman()

play_hangman()
