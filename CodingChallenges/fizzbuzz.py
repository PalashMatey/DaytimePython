def fizzBuzz( n):
        """
        :type n: int
        :rtype: List[str]
        """
        finalList = []
        for num in range(1,n+1):
            if((num%3==0) and (num%5==0)):
                finalList.append("FizzBuzz")
                
            elif (num%3 == 0):
                finalList.append("Fizz")
            elif(num%5 == 0):
                finalList.append("Buzz")
            else:
                finalList.append(str(num))
        print finalList
        #return finalList
answer = fizzBuzz(15)
