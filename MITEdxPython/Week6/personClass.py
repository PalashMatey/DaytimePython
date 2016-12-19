import datetime

class Person(object):
    def __init__(self,name):
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]

    def getLastName(self):
        return self.lastname
    
    def setBirthday(self,day,month,year):
        self.birthday = datetime.date(year,month,day)
        
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self,other):
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname

    def __str__(self):
        return self.name

# me = Person("Palash Sushil Matey")
# print me
# me.getLastName()
# me.setBirthday(06,06,1992)

# print me.getAge()
# #print me.lastname
# her = Person("Chandni Sarda")
# her.getLastName()
# pList = [her, me]
# for p in pList:
#     print p
# pList.sort()
# for p in pList:
#     print p

