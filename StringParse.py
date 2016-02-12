order = "salad water hamburger salad hamburger lol"
order2 = "crap crap"

def item_list(order):
	mylist = order.split(" ")
	salad = []
	water = []
	hamburger = []
	
	for item in mylist:
		if item == 'salad':
			salad.append(item)
		elif item == 'hamburger':
			hamburger.append(item)
		elif item == 'water':
			water.append(item)
		else:
			print 'None of the item are present'
	
	
	print 'Number of salad : ' + str(len(salad))
	print 'Number of hamburger: '+ str(len(hamburger))
	print 'Number of water: '+ str(len(water))
item_list(order)
item_list(order2)
