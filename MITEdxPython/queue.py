class Queue(object):
	def __init__(self):
		self.vals = []
		self.front = 0
		self.rear = 0
	def insert(self,e):
		self.vals.append(e)
		self.rear = self.rear +1
	def remove(self):
		if len(self.vals) == 0:
			print 'Queue is empty'
		else:
			return self.vals.pop(0)
			self.front = self.front + 1
			try:
				if self.front > self.rear:
					print 'Queue is empty'
			except e:
				print e
