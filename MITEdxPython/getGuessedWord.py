def getGuessedWord(secretWord, lettersGuessed):
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
    print character_list
    c = ''.join(character_list)
    return c
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)
