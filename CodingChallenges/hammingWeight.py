def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    return bin(n).count('1')
answer = hammingWeight(00000000000000000000000000001011)
print answer