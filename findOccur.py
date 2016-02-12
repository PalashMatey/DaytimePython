s = 'azcbobobegghabob'
count = 0
for i in range(	0,len(s)-1):
	print i
	if s[i : i+3] == 'bob':
		count = count + 1
print 'The number of bob is: ' + str(count)

