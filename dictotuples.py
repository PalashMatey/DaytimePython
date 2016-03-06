def dict_interdiff(d1,d2):
	toreturn = ()
	rd1 = {}
	rd2 = {}
	if len(rd1)<len(rd2):
		for i in range(len(d1),len(d2)):
			d1[i]=0
	else:
		for i in range(len(d2),len(d1)):
                        d2[i]=0
	print d1
	print d2
	for (i1,n1),(i2,n2) in zip(d1.items(),d2.items()):
		if i1 == i2:
			rd1[i1] = n1+n2
		else:
			if i1<i2:
				rd2[i1]= n1
				rd2[i2]= n2
			else:
				rd2[i2]= n2
				rd2[i1]= n1
	print rd1
	print rd2
	toreturn+(rd1,rd2)
	return toreturn
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
ans = dict_interdiff(d1,d2)
print ans
