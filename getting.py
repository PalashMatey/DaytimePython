def get(hand):
    newdic = hand.copy()
    newlist = []
    for n in newdic:
        while newdic[n]>0:
                newlist.append(n)
                newdic[n] = newdic[n]-1
    c = ''.join(newlist)
    return len(c)
hand = {'a':2,'b':5,'c':0}
x = get(hand)
print x
