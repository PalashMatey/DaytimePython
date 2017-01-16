def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    dict1 = {}
    dict2 = {}
    result = []
    for i in nums1:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in nums2:
        if i in dict2.keys():
            dict2[i] += 1
        else:
            dict2[i] = 1
    for ele in nums1:
        if ele in dict2.keys():
            if dict2[ele] > 0:
                result.append(ele)
                dict2[ele] -= 1          
    return result
list1 = [1,2,2,1]
list2 = [2,2]
answer = intersect(list1,list2)