
def isPalindrome(aString):
	if len(aString)<=2:
		return True
	else:
		return aString[0]==aString[-1] and isPalindrome(aString[1:-1])

aString = raw_input('Enter the string to check for palindrome: ')
aString = aString.lower()
ans = isPalindrome(aString)
print ans
