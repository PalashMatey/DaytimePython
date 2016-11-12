def isAnagram( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictStore = {}
        dictStore2 = {}
        for characters in s:
            if characters in dictStore:
                dictStore[characters] += 1
            else:
                dictStore[characters] = 1
        for charaters2 in t:
            if(charaters2 in dictStore):
                dictStore[charaters2] -= 1

        for characters2 in t:
            if characters2 in dictStore2:
                dictStore2[characters2] += 1
            else:
                dictStore2[characters2] = 1 
        for v in dictStore.values():
            if (v>0):
                return False
        for v in dictStore2.values():
            if (v > 0):
                return False
        return True

answer = isAnagram("a","ab")
print answer