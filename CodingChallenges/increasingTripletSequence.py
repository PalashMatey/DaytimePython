from array import *
def increasingTripletSequence(nums, k):
    try:
        inc = [float('inf')] *(k-1)
        for x in nums:
            inc[bisect.bisect_left(inc,x)] = x
            print inc
        return k == 0
    except:
        return True


ans = increasingTripletSequence([1,2,3,4,5], 3)
print ans