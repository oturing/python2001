#!/python/python

NUM_LINS = 9
NUM_COLS = 12
COLS = map(lambda col: chr(ord('A')+col), range(NUM_COLS))
LINS = range(1,NUM_LINS+1)
print COLS
print LINS

class Market:
	def __init__():
		self.companies = []
	def __len__():
		return len(self.companies)
	def __getitem__(i):
		return self.companies[i]

class Position:
	def __init__():
		pass
		

class Company:
	def __init__(name, pos1, pos2):
		'''	name: company name (must be unique in market)
			t_position: tuple with 2 initial positions
		'''
		self.name = name
		self.positions = []
		self.add_position(pos1)
		self.add_position(pos2)

	def validade_position():
		pass
		
		