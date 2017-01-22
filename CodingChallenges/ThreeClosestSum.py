import itertools
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    final = []
    for i in itertools.permutations(nums,3):
        final.append([abs(sum(i)-target),sum(i)])
    return min(final)[1] 

answer = threeSumClosest([-1,2,1,-4],1)
print answer