import string
def getAvailableLetters(lettersGuessed):
	all = string.ascii_lowercase
	leftout = []
	for letter in all:
		if letter not in lettersGuessed:
			leftout.append(letter)
	c = ''.join(leftout)
	return c
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)
