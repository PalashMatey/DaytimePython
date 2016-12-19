import personClass

class ColumbiaPerson(personClass.Person):
    nextIdNum = 0
    def __init__(self,name):
        personClass.Person.__init__(self,name)
        self.idNum = ColumbiaPerson.nextIdNum
        ColumbiaPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self,other):
        return self.idNum < other.idNum

p1 = ColumbiaPerson('Eric')
p2 = ColumbiaPerson('John')
p3 = ColumbiaPerson('John')
p4 = personClass.Person('John')

print p1.getIdNum()
print p2.getIdNum()
print p1 < p2
print p3 < p2
print p4 < p1 #Comparing Names here
#print p1 < p4 #Compares IdNum here