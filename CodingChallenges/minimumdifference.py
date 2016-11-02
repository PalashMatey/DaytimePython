

import sys

def minMutation( start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        flag = False
        if not bank:
            return -1
        for stringPresent in bank:
            if(stringPresent == end):
                print "Present in bank"
                flag = True
        sum = 0
        dictStart = {}
        dictEnd = {}
        dictResult = {}
        if(flag == True):
            for ele in start:
                if ele in dictStart:
                    dictStart[ele] += 1
                else:
                    dictStart[ele] = 1
            print "Dict Start: ", dictStart
            for ele2 in end:
                if ele2 in dictEnd:
                    dictEnd[ele2] += 1
                else:
                    dictEnd[ele2] = 1
            print "Dict End: " , dictEnd
        else:
            return -1
        for (k,v),(k2,v2) in zip(dictStart.items(),dictEnd.items()):
            if(k == k2):
                dictResult[k] = abs(v-v2)
            else:
                dictResult[k] = v
            print "Dict Result: ", dictResult
        for eleResult in dictResult:
            if (dictResult[eleResult] > 0):
                sum = sum + dictResult[eleResult]
            
        return sum/2

returnedSum = minMutation("AACCGGTT","AAACGGTA",["AACCGGTA", "AACCGCTA", "AAACGGTA"])

print returnedSum

