# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    c = 0
    n = len(secretWord)
    for letter in lettersGuessed:
        if letter in secretWord:
            n = n -1
            if n == 0:
                return True
    return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    character_list = []

    # Go through each letter in secret word to check if we've guessed it
    for letter in secretWord:
        if letter in lettersGuessed:
            # If we've guessed it, we want to display it
            character_list.append(letter)
        else:
            # If we haven't guessed it, we want to display a dash
            character_list.append('_')
    # Turn it into a string and return that string
    c = ''.join(character_list)
    return c


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    # FILL IN YOUR CODE HERE...
    import string
    all = string.ascii_lowercase
    leftout = []
    for letter in all:
	if letter not in lettersGuessed:
		leftout.append(letter)
    c = ''.join(leftout)
    return c

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the Game, Hangman'
    print 'I am thinking of a word this is '+ str(len(secretWord)) + ' long'
    letterGuessed = []
    num_guess = 8
    while(num_guess>0):
	print 'You have '+ str(num_guess) + ' guesses left'
	print 'Available Letters: '+ str(getAvailableLetters(letterGuessed))
	letter = raw_input('Please guess a letter: ')

	if letter in letterGuessed:
		print 'Opps!YOu have already guessed that letter'
		num_guess = num_guess + 1
	else:
		letterGuessed.append(letter)

	if letter in secretWord:
		print 'Good guess: ' +  getGuessedWord(secretWord,letterGuessed)
	else:
		print 'That letter is not in my word: ' + getGuessedWord(secretWord,letterGuessed)

	if getGuessedWord(secretWord,letterGuessed) == secretWord :
		print 'Congratulations you win!'
		exit()
	#if (secretWord == c):
	#	print 'Congratulations You won'
	#	break
	#if  (isWordGuessed(secretWord,letterGuessed)) == True:
	#	print 'Congratulations you won'
	#	exit()
	num_guess = num_guess - 1	
	if num_guess == 0:
		print 'Sorry you ran out of guesses..'
		print 'The correct word is ' + secretWord
		exit()





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
