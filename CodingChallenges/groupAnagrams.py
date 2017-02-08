import itertools
def groupAnagrams(strs):
    ListofDict = []
    for s in strs:
        anadict = {}
        for char in s:
            anadict[char] = anadict.get(char,0) + 1
        ListofDict.append([anadict,s])
    getGroupAnagrams(ListofDict)
def getGroupAnagrams(ListofDict):
    # print ListofDict
    finalList = []
    for i in range(len(ListofDict)):
        
        temp = []
        temp.append(ListofDict[i][1])
        for j in range(i+1,len(ListofDict)):
            if ListofDict[i][0] == ListofDict[j][0]:
                temp.append(ListofDict[j][1])
                #ListofDict.remove(ListofDict[j])
        finalList.append(temp)
    print finalList            
            
    
        
    
    
        



    
            
    


answer = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])