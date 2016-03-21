x = int(raw_input('Enter the intger: '))
def ndigits(x):
	x = abs(x)
	if x<9:
		return 1
	else:
		return 1+ ndigits(x/10)

c = ndigits(x)
print "The number of digits are: " + str(c)
