def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if(needle == ""):
            return 0
        for i in range(0,len(haystack)+1):
            print haystack[:i]
            if (needle in haystack[:i]):
                return i - len(needle)
        return -1 

answer = strStr("mississippi","issi")
print answer
