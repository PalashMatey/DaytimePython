def dict_interdiff(d1,d2):
	toreturn = ()
	rd1 = {}
	rd2 = {}

	for (i1,n1),(i2,n2) in zip(d1.items(),d2.items()):
		print 'D1 index,value pair is: ' + str(i1)+ ' '+str(n1)
		print 'D2 index,value pair is: ' + str(i2)+ ' '+str(n2)
		if i1 == i2:
			rd1[i1] = n1+n2
		else:
			if i1 not in d2.keys():
				rd2[i1]= n1
				print 'i1 not in d2'
				#rd2[i2]= n2
			if i2 not in d1.keys():
				rd2[i2]= n2
				print 'i2 not in d1'
				#rd2[i1]= n1
	print rd1
	print rd2
	toreturn+(rd1,rd2)
	return toreturn
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
ans = dict_interdiff(d1,d2)
print ans
