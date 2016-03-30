class Grades(object):
	'''A mapping of students to the grade'''
	def __init__(self):
		self.students = []
		self.grades = {} #map id number to the grades
		self.isSorted = True #True if students are sorted
	def addStudent(self,student):
		if student in self.students:
			raise ValueError('Duplicate Student')
		self.students.append(student)
		self.grades[student.getIdNum()]=[]
		self.isSorted = False
	def addGrade(self,student,grade):
		try:
			self.grade[student.getIdNum()].append(grade)
		except KeyError:
			raise ValueError('Student not in grade book')
	def getGrades(self,student):
		try: # returning a copy of the grades
			return self.grades[student.getIdNum()][:]
		except KeyError:
			raise ValueError('Student is not in the gradebook')
	def allStudents(self):
		if not self.isSorted:
			self.students.sort()
			self.isSorted = True
		return self.students[:]
	def gradeReport(course):
		report = []
		for s in course.allStudents():
			tot = 0.0
			numGrades = 0
			for g in getGrades(s):
				tot +=g
				numGrades +=1
			try:
				average = tot/numGrades
				report.append(str(s)+'mean grade is'+str(average))
			except ZeroDivisionError:
				report.append(str(s)+'has no grades')
		return '\n'.join(report)
	
