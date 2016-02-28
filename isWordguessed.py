def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in 
lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    c = 0
    n = len(secretWord)
    for i in lettersGuessed:
        if i in secretWord:
            n = n -1
            print 'Correctly guessed: ' + i
            if n == 0:
                return True
    return False   
                
secretWord = 'apple'
lettersGuessed = ['e', 'a', 'p', 'p', 'r', 'l']
print isWordGuessed(secretWord, lettersGuessed)
