def sorted_search(elements,target):
    if not elements or len(elements) <= 0:
        return -1
    left = 0
    right = len(elements) - 1
    while left < right:
        middle = (left + right + 1)/2
        if elements[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    if elements[right] == target:
        return right
    return -1

#n = [3,6,1,12,123,45,36,234,356,7,23]
n = [1,2,3,4,5,6,7,8,9,10]
ans = sorted_search(n,3)
print ans

