a = int(raw_input('Enter a number:  '))
b = int(raw_input('Enter the second number: '))
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    a1 = a
    b1= b
    if a>=b:
        if (a%b==0 and b1%b==0):
            return b
        else:
            return gcdIter(a,b-1)
    else:
        if (b%a==0 and a1%a==0) :
            return a
        else:
            return gcdIter(b,a-1)


z= gcdIter(a,b)
print str(z)
