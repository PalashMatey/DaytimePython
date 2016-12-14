res = []
def genSubsets1(L = [1,2,3]):
    
    print len(L)
    if len(L) == 0:
        
        return [[]]
    print 'getting the smaller element'
    print L[:-1]
    res.append(genSubsets1(L[:-1]))
    
    print res

    #print smaller



genSubsets1()