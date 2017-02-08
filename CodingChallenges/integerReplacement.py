def integerReplacement(n):
    if n == 1:
        return 0
    if n%2:
        return 1 + min(integerReplacement(n+1),integerReplacement(n-1))
    else:
        return 1 + integerReplacement(n/2)
answer = integerReplacement(10)
print answer
