def flatten(aList):
	newlist = []
	for i in aList:
		if isinstance(i,list):
			for j in i:
				newlist.append(j)
		else:
			newlist.append(i)
	return newlist

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
hel = flatten(aList)
print hel
