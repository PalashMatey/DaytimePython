import heapq
def thirdMax(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print nums
        print 'The maximum number in the list is',max(nums)
        nums = set(nums)
        print 'After the set is made', nums
        print 'The max number in the set is',max(nums)
        l = [float('-inf')] * 3
        print 'The heap is defined',l
        for n in nums:
            if n > l[0] and n not in l:
            
                print heapq.heappushpop(l, n)
        #return l[0] if l[0] != float('-inf') else max(l)
        #Bascially O(n) means that I can go through the array just once

listOfNumbers = [1,2,3,4,5]
thirdMax(listOfNumbers)