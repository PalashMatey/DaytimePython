class Queue(object):
	def __init__(self):
		self.vals = []
		self.front = 0
		self.rear = 0
	def __str__(self):
		return self.vals
	def insert(self,e):
		self.vals.append(e)
		self.front = self.front +1
		self.front = self.rear
