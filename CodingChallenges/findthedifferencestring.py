def findTheDifference( s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for ch in t:
            if ((s+t).count(ch)%2 == 1):
                return ch
#Easiest way to find the odd one out.
answer = findTheDifference("abcd","abcde")
print answer