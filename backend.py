class main():

	def __init__(self):
		self.random_word = ''
		self.display_string = []
		self.used_alphabets = []

	def get_random_word(self):
		return 'HANGMAN IS AMAZING' #write a function that gets word from a external text file or scrapes from the web

	def create_display_string(self): #This function creates the string that is to be displayed
		self.random_word = list(self.get_random_word()) #converting the actual word from a string to a list for convenience
		word_length = len(self.random_word) #getting the length of actual word to know how many underscores to use

		for i in range(word_length):
			self.display_string.append('_ ') #creating the display string which only has underscores


	def change_display_string(self, actual_word, display_string, revealed_alphabet):
		while revealed_alphabet in  actual_word:
			index = actual_word.index(revealed_alphabet) #getting the index of the alphabet in the actual word
			actual_word[index] = '0' #changing that index so that it doesn't repeat
			display_string[index] = revealed_alphabet+' ' #displaying the revealed alphabet on the screen

		return display_string

		#this function replaces __ es with the alphabet selected

	def check_input(self, letter_input):

		letter_input = letter_input[0]

		if letter_input in self.used_alphabets: #if the input has been used before
			pass
		else: #if the input has not been used before
			self.used_alphabets.append(letter_input)

		if letter_input in self.random_word: #if the input is correct
			self.display_string = self.change_display_string(self.random_word, self.display_string, letter_input) #change the display string

		else: #if the input is not correct			
			pass #cut a life since you guessed it wrong

