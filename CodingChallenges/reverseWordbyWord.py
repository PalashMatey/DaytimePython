def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    ary = s.split()
    reverseList = []
    for i in xrange(len(ary)):
        reverseList.append(ary.pop())
        reverseList.append(' ')
    return ''.join(reverseList)[:-1]
        


answer = reverseWords("The Sky is Blue")
print answer