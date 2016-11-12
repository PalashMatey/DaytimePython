def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictStore = {}
        for i,num in enumerate(numbers):
            if((target-num) in dictStore):
                return (dictStore[target-num]+1),i+1
            dictStore[num] = i
                    
        


answer = twoSum([2,3,4],6)
print answer
# for i in range(0,len(numbers)):
        #     if ((target - numbers[i]) in dictStore.keys():
        #         return i+1
        # for (k,v) in dictStore.items():
            