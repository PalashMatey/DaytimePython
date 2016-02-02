class PartyAnimal:
	x = 0
	name = ""
	def __init__(self,nam):
		self.name = nam
		print self.name,"I am constructed"
	def party(self):
		self.x = self.x + 1
		print self.name ,"party count",self.x
	def __del__(self):
		print "I am destructed" , self.x
an = PartyAnimal("Palash")

an.party()
an.party()
an.party()
	
print "Type", type(an)
print "DIR" , dir(an)

class FootballFan(PartyAnimal):
	points = 0
	def touchdown(self):
		self.points = self.points + 7
		self.party()
		print self.name, "points", self.points

j = FootballFan("Jim")
j.party()
j.touchdown()
