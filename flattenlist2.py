newlist = []
def flatten(aList):
	global newlist
	for i in aList:
		if isinstance(i,list):
			flatten(i)
		else:
			newlist.append(i)
	return newlist


aList = [[3], [2, 1, 0], [4, 5, 6, 7]]
print aList
hel = flatten(aList)
print hel
