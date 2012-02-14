# Tombola_test.py

import unittest
from Tombola import Tombola, TombolaVazia, AutoTombola
import whrandom
from time import time, sleep

rndres = []

class Teste_Tombola(unittest.TestCase):
	def setUp(self):
		gera_rand = whrandom.whrandom(1,1,1) # assegurar séries aleatórias idênticas
		self.fnrand = gera_rand.random
		self.t10 = Tombola(range(10), whrandom.whrandom(1,1,1).random)

	def teste_fnrand(self):
		rndres = [0.0169309061997, 0.895253911238, 0.111491021216, 0.939526796411, 0.128229855101,
					0.178003992983, 0.299827082495, 0.349718406372, 0.0592874602539, 0.821979314656]
		for i in xrange(len(rndres)):
			rnd = self.fnrand()
			assert str(rndres[i]) == str(rnd), 'séries aleatórias diferem: %s != %s' % (rndres[i], rnd)

	def teste_repr(self):
		t = Tombola([1])
		assert repr(t) == '[1]'

	def teste_len(self):
		t = Tombola([1])
		assert len(t) == 1

	def teste_len2(self):
		for i in [2,4,10,100,1000,23456]:
			t = Tombola(range(i))
			assert len(t) == i

	def teste_init(self):
		t = Tombola(range(3), self.fnrand)
		assert repr(t) == '[0, 2, 1]'
		assert len(t) == 3

	def teste_init2(self):
		t = Tombola(('abacate', 'banana', 'caju'), self.fnrand)
		assert repr(t) == "['abacate', 'caju', 'banana']"
		assert len(t) == 3

	def teste_init3(self):
		t = Tombola('XYZ', self.fnrand)
		assert repr(t) == "['X', 'Z', 'Y']"
		assert len(t) == 3

	def teste_misturar(self):
		self.t10.misturar(self.fnrand)
		assert repr(self.t10) == "[0, 1, 2, 5, 6, 7, 9, 3, 8, 4]"

	def teste_misturar_1(self):
		t = Tombola([1])
		str0 = repr(t)
		t.misturar()
		assert repr(t) == str0

	def teste_misturar_1000(self):
		t = Tombola(range(1000))
		str0 = repr(t)
		t.misturar()
		# existe a minúscula chance de 1:1000! (1 para fatorial de 1000)
		# de que o resultado seja idêntico por acaso...
		assert repr(t) != str0

	def teste_sortear(self):
		lt_res = [0, 8, 2, 4, 5, 6, 7, 9, 1, 3]
		lt_res.reverse() # sortear() usa pop(), que funciona do fim para o começo
		t = Tombola(range(10), self.fnrand)
		for i in range(len(t)):
			res = t.sortear()
			assert lt_res[i] == res, '%s != %s' % (lt_res[i], res)

	def teste_call(self):
		lt_res = [0, 8, 2, 4, 5, 6, 7, 9, 1, 3]
		lt_res.reverse() # sortear() usa pop(), que funciona do fim para o começo
		t = Tombola(range(10), self.fnrand)
		for i in range(len(t)):
			res = t()
			assert lt_res[i] == res, '%s != %s' % (lt_res[i], res)

	def teste_sortear_exception(self):
		t = Tombola(range(3))
		t.sortear()
		t.sortear()
		t.sortear()
		self.assertRaises(TombolaVazia, t.sortear)

class Teste_AutoTombola(unittest.TestCase):
	def teste_refil(self):
		t = AutoTombola(range(3))
		for i in range(1000):
			t()

	def teste_anti_repeticao1(self):
		t = AutoTombola(range(2))
		ult_res = None
		for i in range(100):
			prim_res = t()
			assert prim_res != ult_res
			ult_res = t()

	def teste_anti_repeticao2(self):
		qt_bolas = 200
		t = AutoTombola(range(qt_bolas))
		ult_res = None
		for i in range(100):
			prim_res = t()
			assert prim_res != ult_res
			for j in range(qt_bolas-2): t()
			ult_res = t()


def suite():
	suite1 = unittest.makeSuite(Teste_Tombola, 'teste_')
	suite2 = unittest.makeSuite(Teste_AutoTombola, 'teste_')
	return unittest.TestSuite((suite1, suite2))

if __name__ == '__main__':
	unittest.TextTestRunner().run(suite())

