

import sys

def minMutation( start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        flag = False
        for stringPresent in bank:
            if(stringPresent == end):
                print "Present in bank"
                flag = True
            else:
                flag = False
        sum = 0
        dictStart = {}
        dictEnd = {}
        dictResult = {}
        if(flag == True):
            for ele in start:
                if ele in dictStart:
                    dictStart['ele'] += 1
                    print "Added to increment " ,ele,  dictStart['ele']
                else:
                    dictStart['ele'] = 1
                    print "Start values of element " ,ele, dictStart['ele']
            for ele2 in end:
                if ele2 in dictEnd:
                    increment = dictEnd['ele2']
                    increment = increment + 1
                    dictEnd['ele2'] = increment
                else:
                    dictEnd['ele2'] = 1
                    print "End Values of the Element", ele2, dictEnd['ele2']
        for (k,v),(k2,v2) in zip(dictStart.items(),dictEnd.items()):
            if(k == k2):
                dictResult[k] = abs(v-v2)
                print k,dictResult[k]
        for eleResult in dictResult:
            if (dictResult[eleResult] > 0):
                sum = sum + dictResult[eleResult]
            
        return sum

returnedSum = minMutation("AACCGGTT","AACCGGTA",["AACCGGTA"])
print returnedSum

