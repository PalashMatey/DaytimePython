def updateHand(hand,word):
	currentlist = hand.copy()
    	for i in word:
        	if i in hand.keys():
                	currentlist[i] = currentlist[i] - 1
    	return currentlist
def main():
	x = raw_input('enter shit: ')
	hand = {'p':3,'o':4,'t':2}
	hand = updateHand(hand,x)
	print hand
main()
