def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    finalStr = ''
    if not '[' or not ']' in s:
        return s
    for char in s:
        
        if char.isdigit():
            multi = int(char)
        if char == '[':
            newStr = ''
        if char.isalpha():
            newStr = newStr + char
        if char == ']':
            finalStr = finalStr + multi * newStr
        
        
    return finalStr
        
answer = decodeString('3[a]2[bc]')
print answer