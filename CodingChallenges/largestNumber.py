def largestNumber(num):
    comp = lambda a,b: 1 if a+b> b+a else -1 if a+b<b+a else 0
    num = map(str,num)
    num.sort(cmp = comp, reverse = True)
    print num 


largestNumber([3,30,34,5,9])


