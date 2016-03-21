print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door= raw_input(">")

if door == "1":
	print "There is a bear eating the cake"
	print "1.Take the cake"
	print "2.Scream at the bear"
	
	bear= raw_input('>')
	
	if bear== '1':
		print "The bear eats your face off."
	elif bear =='2':
		print "The bear eats your legs off."
	else:
		print "Well doing %s is probably better." % bear
	
elif door== '2': 
	print "You stare into the endless abysss of berries"
	print "1.Blueberries"
	print "2.Yellow jacket clothespin"
	print "3.Understanding revolvers yelling melodies"
	
	insanity= raw_input(">")
	
	if insanity == '1' or insanity == '2':
		print "Your body survives powered by mind of jello"
	else:
		print "The insanity rots your eyes into a pool of muck"
	
else:
	print "You stumble and fall on a knife and die"
	

	