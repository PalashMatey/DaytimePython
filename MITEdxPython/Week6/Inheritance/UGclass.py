import ColumbiaPerson

class UG(ColumbiaPerson.ColumbiaPerson):
    def __init__(self,name,classYear):
        ColumbiaPerson.ColumbiaPerson.__init__(self,name)
        self.year = classYear
    
    def getClass(self):
        return self.year

class Grad(ColumbiaPerson.ColumbiaPerson):
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)

s1 = UG('Fred', 2016)
s2 = Grad('Angela')
print isStudent(s1)
print isStudent(s2)
