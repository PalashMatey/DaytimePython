def twoSum(nums, target):
    dic = {}
    for i, n in enumerate(nums):
	print i,n,nums
	print dic 
        if n in dic:
            return [dic[n], i]
        dic[target-n] = i
nums = [1,2,3,4,5,6,7]
target = 13
hel = twoSum(nums,target)
print hel
