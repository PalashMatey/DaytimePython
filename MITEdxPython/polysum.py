import math
'''
Importing the math module, in order to access the tan function.
Calculating the area and perimeter, summing it up and returning the rounded value
'''
def polysum(n,s):
    c = math.pi
    area = (0.25*n*s**2)/math.tan(c/n)
    perimeter = (n*s)**2
    
    sum = area + perimeter
    return round(sum,4)
