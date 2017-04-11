
def commonTradingTime(L1,L2):
    
    sum = 0
    for x1,x2 in sorted(L1,key = lambda x:x[0]):
        for y1,y2 in sorted(L2, key = lambda y:y[0]):
            if is_overlapping(x1,x2,y1,y2):
                sum += min(x2,y2) - max(x1,y1)
    return sum

def is_overlapping(x1,x2,y1,y2):
    return max(x1,y1) <= min(x2,y2) 
 




L1 = [(5,9.5),(1,3),(10.2,13),(12,16.4),(17,19)]
L2 = [(2,6),(8,10),(11,15),(16.5,17.5),(20,21)]

L3 = [(1,2.5),(2.7,4),(3,5.6),(9,11),(13,18)]
L4 = [(0,13),(8,15),(13.5,14.5),(16,19)]
ans = commonTradingTime(L3,L4)
print ans