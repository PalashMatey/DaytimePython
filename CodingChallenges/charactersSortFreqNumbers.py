from collections import OrderedDict
def sortByFrequency(s):
    if s is None:
        return 
    st = ''
    dictstart = {}
    for i in s:
        dictstart[i] = dictstart.get(i,0) + 1
    for key,value in sorted(dictstart.items()):
        st = st + key * value
    print st
sortByFrequency("cdddddaaabbbbccccddd")