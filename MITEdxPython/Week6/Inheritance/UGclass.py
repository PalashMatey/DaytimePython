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

# s1 = UG('Fred', 2016)
# s2 = Grad('Angela')
# print isStudent(s1)
# print isStudent(s2)

class Grades(object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
    
    def addStudent(self,student):
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.getIdNum()] = {}
        self.isSorted = False
    
    def addGrade(self,student,grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in gradebook')
        
    def getGrades(self,student):
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in grade book')
    
    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
    
def GradeReport(course):
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is '
                          + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)

        
ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('John Henry')
g2 = Grad('George Steinbrenner')

six00 = Grades()
six00.addStudent(g1)

six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)

for s in six00.allStudents():
    six00.addGrade(s,75)

six00.addGrade(g1, 100)
six00.addGrade(g2, 25)

six00.addStudent(ug3)
