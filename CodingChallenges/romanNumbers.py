def romanNumbers(s):
        """
        :type nums: List[int]
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        sum = 0
        stack = []
        stack.append(s[0])
        for i in range(0,len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:

                sum = sum  - roman[s[i]]

            else:

                sum = sum + roman[s[i]]


        sum = sum + roman[s[len(s)-1]]
        
                
        # for ch in s[1:]:
        #     if ch in roman.keys():
        #         temp = stack.pop()
        #         if roman[temp] < roman[ch]:                    
        #             sum = sum + (roman[ch] - roman[temp])
        #         else:
        #             sum = sum + roman[temp] + roman[ch]
        
        print sum
                
        #return l[0] if l[0] != float('-inf') else max(l)
        #Bascially O(n) means that I can go through the array just once


romanNumbers("MCMXCVI")
    




