def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    stack.append(["",1])
    num = ""
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == '[':
            stack.append(["",int(num)])
            print 'On open this is what is displayed'
            print stack
            num = ""
        elif ch == ']':
            st, k = stack.pop()
            print 'This one is on close', st,k
            stack[-1][0] = st * k
            print 'The stack now', stack
        else:
            stack[-1][0] += ch
             
    return stack[0][0]
answer = decodeString('3[a]2[bc]')
print answer