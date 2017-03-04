# def decodeString(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     finalStr = ''
#     if not '[' or not ']' in s:
#         return s
#     for char in s:
        
#         if char.isdigit():
#             multi = int(char)
#         if char == '[':
#             newStr = ''
#         if char.isalpha():
#             newStr = newStr + char
#         if char == ']':
#             finalStr = finalStr + multi * newStr
        
        
#     return finalStr
def decodeString(s):
    stack = []
    stack.append(['',1])
    print stack
    num = ''
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == '[':
            print 'Open bracket',
            stack.append(['',int(num)])
            num = ''
        elif ch == ']':
            st, k = stack.pop()
            stack[-1][0] += st * k
            print 'Close bracket',
            print stack
        else:
            stack[-1][0] += ch
            print stack
answer = decodeString('3[a]2[bc]')
print answer