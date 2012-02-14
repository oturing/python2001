#!/usr/bin/python

'''	tombola.py: classe para sortear itens de uma lista sem repetir
 	v. 2.0:
 		- sorteia itens de qualquer sequência que possa ser convertida com list()
 	    - trabalha sobre uma cópia local da lista
'''

import whrandom

class TombolaVazia(Exception):
	pass

class Tombola:
	def __init__(self, bolas, fnrandom=None):
		# fnrandom deve ser uma função geradora de floats aleatórios
		# que é utilizada apenas no método misturar()
		assert len(bolas) > 0
		self.__bolas = list(bolas)
		self.misturar(fnrandom)

	def listar_bolas(self):
		return self.__bolas

	def misturar(self, fnrandom=None):
		# em testes, fnrandom deve ser uma função
		# que gere uma série repetível de números
		if fnrandom == None:
			fnrandom = whrandom.random
		tuplas = []
		for item in self.__bolas:
			tuplas.append( ( fnrandom(), item ) )
		tuplas.sort()
		for i in range(len(self.__bolas)):
			self.__bolas[i] = tuplas[i][1]

	def sortear(self):
		try:
			return self.__bolas.pop()
		except IndexError: #pop from empty list
			raise TombolaVazia, 'não há mais elementos para sortear'

	def __repr__(self):
		return repr(self.__bolas)

	def __len__(self):
		return len(self.__bolas)

	def __getitem__(self, i):
		return self.__bolas[i]

	def __call__(self, *args):
		return apply(self.sortear, args)

class AutoTombola(Tombola):
	'''	tombola com reinicio automatico depois de sortear a última bola
	'''

	def __init__(self, bolas, fnrandom=None):
		# AutoTombola rejeita repetições na mudança de séries
		# por isso precisa de no mínimo dois itens diferentes.
		if len(bolas) < 2:
			raise ValueError, 'a lista deve ter no minimo dois itens'
		if bolas[0] == bolas[1]:
			bolas.sort()
			if bolas[0] == bolas[-1]:
				raise ValueError, 'a lista deve conter ao menos um item diferente dos demais'
		self.__bolas_bkp = bolas[:]
		Tombola.__init__(self, bolas)
		self.__bola_anterior = None

	def sortear(self):
		try:
			bola = Tombola.sortear(self)
			self.__bola_anterior = bola
			return bola
		except TombolaVazia:
			#lembrar última bola da série anterior
			ultima_bola = self.__bola_anterior
			#reiniciar tombola
			self.__init__(self.__bolas_bkp)
			#evitar repetição na passagem de uma série para a próxima
			#self[-1] é a próxima a ser sorteada
			while self[-1] == ultima_bola:
				self.misturar()
			return Tombola.sortear(self)


if __name__ == '__main__':
	print "\n\n"

	t = AutoTombola(list('ABCDE'))
	print 't == ', t
	print 'len(t) == ', len(t)

	t.misturar()
	print 't == ', t

	print t.sortear()
	print 't == ', t

	print t()
	print 't == ', t

	t.misturar()
	print t()
	print 't == ', t

	print t()
	print 't == ', t

	print 'proxima bola: ', t[-1]
	print 'ultima bola: ', t[0]

	print 'bolas restantes:',
	for i in t:
		print i,

	print "\n\n"

	#teste AutoTombola
	while 1:
		bola = t()
		print bola, len(t)


