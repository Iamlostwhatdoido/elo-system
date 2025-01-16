class Sortable:
	def __init__(self, name, score, doubt):
		self.name = name
		self.score = score
		self.doubt = doubt
		
	def rename(self, new_name):
		self.name = new_name