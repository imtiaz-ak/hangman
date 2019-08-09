
def get_random_word():
	return 'DOG' #write a function that gets word from a external text file or scrapes from the web

def change_display_string(actual_word, display_string, revealed_alphabet):
	while revealed_alphabet in actual_word:
		#replace all the underscores with the letters on the word

		#get the index of the revealed alphabets in the actual word
		#then replace the index of the display string of thoses indexes with the revealed alphabet
		index = actual_word.index(revealed_alphabet)
		actual_word[index] = 0
		display_string[index] = revealed_alphabet


	return display_string



#Getting a random word to run the game
random_word = list(get_random_word())
word_length = len(random_word) #The length is used to create the display string

display_string = ''

for i in range(word_length):
	display_string += '_'

display_string = list(display_string)

print(display_string)
print(type(random_word))
print(random_word)


#Taking the input and matching with the word
used_alphabets = []

while True:

	letter_input = input("Enter an alphabet: ") #Taking the input

	if letter_input in used_alphabets: #if the input has been used before
		pass
	else: #if the input has not been used before
		used_alphabets.append(letter_input)

		if letter_input in random_word: #if the input is correct
			display_string = change_display_string(random_word, display_string, letter_input) #change the display string
			print(display_string)

		else: #if the input is not correct			
			pass #cut a life since you guessed it wrong



