def dict_interdiff(d1,d2):
	toreturn = ()
	rd1 = {}
	rd2 = {}
	for i in d1.keys():
		for j in d2.keys():
			if i == j:
				rd1[i] = d1[i]+d2[j]
			else:
				if i not in d2.keys():
						rd2[i] = d1[i]
				try:
					if j not in d1.keys():
						rd2[j] = d2[j]
				except:
					pass
	toreturn= toreturn + (rd1,rd2)
	return toreturn
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
ans = dict_interdiff(d1,d2)
print ans
