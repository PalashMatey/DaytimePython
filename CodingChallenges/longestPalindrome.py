def longestPalidrome(s):
    res = ''
    count = 0
    for i in xrange(len(s)):
        for k in xrange(2):
            temp = helper(s,i,i+k)
            if len(temp) > 1:
                count += 1
            if len(temp) > len(res):
                res = temp
    return res,count

def helper(s,l,r):
    while l>=0 and r<len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]

ans,count = longestPalidrome('abacaba')
print ans,count