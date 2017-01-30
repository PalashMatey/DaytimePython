def topKFrequent(nums,k):
    if nums is None:
        return

    dictele = {}
    for num in nums:
        dictele[num] = dictele.get(num, 0) + 1

    x = sorted(dictele.values())
    return x[:k]