class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.dp = nums
        for i in xrange(1, len(nums)):
            #print i
            print self.dp[i]
            # print self.dp[i-1]
            self.dp[i] += self.dp[i-1]
        print self.dp

            

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
nums = [2,12,13,4,5,6]
numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)