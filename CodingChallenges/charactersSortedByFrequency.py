def frequencySort(s):
        """
        :type s: str
        :rtype: str
        """
        dictStart = {}
        returnedTupleList = []
        for ele in s.lower():
            dictStart[ele] = dictStart.get(ele,0) + 1
        print dictStart
        sorted_dict = sorted(dictStart.items(),key = lambda x:x[0], reverse=False)
        print sorted_dict
        for w in sorted_dict:
            returnedTupleList.append(w[0] * w[1])
        return ''.join(returnedTupleList)

            

answer = frequencySort("abbbbccbabccaadEEE")
print answer