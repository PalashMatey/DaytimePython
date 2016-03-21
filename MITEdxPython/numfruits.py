def nfruits(dic,seq):
	x = len(seq)
	for i in seq:		
		blacklist=[]
		x = x -1
		if i in dic.keys():
			dic[i] = dic[i]-1
			blacklist.append(i)
			if x==0 :
				print 'Returning in the middle'
				return max(dic.values())
			else:
				for i,n in dic.items():
					if i not in blacklist:
						dic[i] = dic[i]+ 1
	return max(dic.values())			#for dic.keys() not in blacklist:
				#dic[dic.keys()] = dic[dic.keys()] + 1
				#print 'This is other value updates'+ dic



dic = {'A': 5, 'B': 6, 'G': 5, 'M': 7, 'R': 6, 'U': 8, 'T': 9, 'Y': 5}
seq = 'U'
x = nfruits(dic,seq)
print x
