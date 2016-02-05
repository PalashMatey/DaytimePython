

print 'Please think of a number between 0-100!'
low = 0
high = 100
ans = 100/2


while True:

	

	print('Is your secret number? ' + str(ans))
	print 'Enter h to indicate the guess is too high.',
	print 'Enter l to indicate the guess is too low.',
	print 'Enter c to indicate I guessed correctly. ',
	num = raw_input()
	if (num == 'h' or num == 'l' or num == 'c'):
		if num == 'h':
			high = ans
		elif num == 'l':
			low = ans
		else:	
			break
 
	else:
		print 'Sorry, I did not understand your input.'

	ans = (high+low)/2
print('Game over.Your secret number was: ' + str(ans) )
