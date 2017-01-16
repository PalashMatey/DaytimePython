def insertionSort(nums):

    for i in range(1,len(nums)):
        value = nums[i]
        j = i -1
        while j >= 0:
            if nums[j+1] > nums[j]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j+ 1] = temp
            j -= 1

    print nums

insertionSort([24,12,45,1,3,76])