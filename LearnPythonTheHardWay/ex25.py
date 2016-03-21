def break_words(stuff):
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	return sorted(words)
	
def print_first_words(words):
	word= words.pop(0)
	print word

def print_last_words(words):
	word= words.pop(-1)
	print word
	
def sort_sentence(sentence):
	words= break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	words= break_words(sentence)
	print_first_words(words)
	print_last_words(words)

