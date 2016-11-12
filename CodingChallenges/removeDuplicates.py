def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(1,len(nums)):
            if (nums[i] != nums[j]):
                j += 1
                nums[j] = nums[i]

        print j + 1
                



nums = [11,11,12,13,13,13,14,15,16,17]
answer = removeDuplicates(nums)
print answer