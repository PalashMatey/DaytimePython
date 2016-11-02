def frequencySort(s):
        """
        :type s: str
        :rtype: str
        """
        dictStart = {}
        returnedTupleList = []
        for ele in s:
            if ele in dictStart:
                dictStart[ele] += 1
            else:
                dictStart[ele] = 1
        sorted_dict = sorted(dictStart.items(),key = lambda x:x[1], reverse=True)
        for w in sorted_dict:
            returnedTupleList.append(w[0] * w[1])
        return ''.join(returnedTupleList)

            

answer = frequencySort("ababababaaccbabccaa")
print answer