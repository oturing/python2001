#!/usr/bin/env python

'''	tombola.py: classe para sortear itens de uma lista sem repetir
 	v. 2.1:
 		- sorteia itens de qualquer sequencia que possa ser convertida 
 		  em uma lista atraves da funcao com list()
 		- trabalha sobre uma copia local da lista fornecida no construtor
'''

import random

class TombolaVazia(Exception):
	pass

class Tombola:
	def __init__(self, bolas, fnrandom=None):
		'''copiar lista e misturar elementos'''
		# fnrandom deve ser uma funcao geradora de floats aleatorios
		# que e' utilizada apenas no metodo misturar()
		assert len(bolas) > 0, ""
		try:
			self.__bolas = list(bolas)
		except:
			raise TypeError, "nao sei lidar com bolas assim: %s" % bolas
		self.__fnrandom = fnrandom	
		self.misturar()

	def listar_bolas(self):
		'''retornar ref para lista de bolas'''
		return self.__bolas

	def misturar(self):
		'''embaralhar ordem das bolas'''
		# em testes, fnrandom deve ser uma funcao
		# que gere uma serie repetivel de numeros
		if self.__fnrandom is None:
			self.__fnrandom = random.random
		random.shuffle(self.__bolas, self.__fnrandom)

	def sortear(self):
		'''retornar bola do fim da fila'''
		try:
			return self.__bolas.pop()
		except IndexError: #pop from empty list
			raise TombolaVazia, "nao ha' mais elementos para sortear"
			
	def __repr__(self):
		'''retornar repr da lista de bolas'''
		return repr(self.__bolas)

	def __len__(self):
		'''retornar quantidade de bolas nao sorteadas'''
		return len(self.__bolas)

	def __getitem__(self, i):
		'''retornar bola especifica pelo indice'''
		return self.__bolas[i]

	def __call__(self, *args):
		'''invocar sortear()'''
		return apply(self.sortear, args)

class AutoTombola(Tombola):
	'''	tombola com reinicio automatico depois de sortear a ultima bola
	'''

	def __init__(self, bolas, fnrandom=None):
		# AutoTombola evita repeticoes na mudanca de series
		# por isso precisa de no minimo dois itens diferentes.
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
			#lembrar ultima bola da serie anterior
			ultima_bola = self.__bola_anterior
			#reiniciar tombola
			self.__init__(self.__bolas_bkp)
			#evitar repeticao na passagem de uma serie para a proxima
			#self[-1] e' a proxima a ser sorteada
			while self[-1] == ultima_bola:
				self.misturar()
			return Tombola.sortear(self)
			
def sortear(lista):
     return random.choice(lista)			


if __name__ == '__main__':
	print "\n\n"

	t = Tombola('ABCDE')
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
	t = AutoTombola('ABCDE')
	while 1:
		bola = t()
		print bola, len(t)


