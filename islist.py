def dotproduct(listA,listB):
	sum = 0
	for x,y in zip(listA,listB):
		sum = sum + x*y
	return sum
listA = [1, 2, 3]
listB = [4, 5, 6]
ans = dotproduct(listA,listB)
print ans
