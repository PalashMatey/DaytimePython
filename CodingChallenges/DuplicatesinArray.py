def findDuplicates(nums):
        dictStore = {}
        dictResult = []
        for n in nums:
            if n in dictStore:
                dictStore[n] +=1
            else:
                dictStore[n] = 1
        for k,v in dictStore.items():
            if (v>1):
                dictResult.append(k)
        return dictResult

result = findDuplicates([4,3,2,7,8,2,3,1])
print result