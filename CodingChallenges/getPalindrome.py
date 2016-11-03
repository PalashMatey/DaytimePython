def isPalindrome(s):
    
    
    newS= [i.lower() for i in s if i.isalnum()]
    return newS == newS[::-1]


answer = isPalindrome("A man, a plan, a canal: Panama")
print answer