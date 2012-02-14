# dic_util.py

import re
from string import strip, split, lower, replace, maketrans, translate
from hx_latin1 import cars2ascii


TIPO_SIMPLES = 's'
TIPO_LOCUCAO = 'loc'
TIPO_HIFEN = 'hif'
TIPO_SIMBOLO = 'smb'

SEPARADORES = """-_.,:;/\\+"'!|"""

LT_VAZIAS_PT = ['ou','de','da','do','para','por','em','no','na','e','a','o','com']
LT_VAZIAS_EN = ['and','of','for', 'the', 'to', 'at', 'on', 'ou'] #ou está aqui devido a sujeiras em M-XXXX

RE_TAG = re.compile(r'<.*?>')

def remover_duplicatas(lista):
	lt_nova = []
	for pal in lista:
		if not pal in lt_nova: lt_nova.append(pal)
	return lt_nova		

def so_az(texto):
	# retorna 1 se texto só tem letras de 'a' a 'z' (minusculas)
	# retorna 0 se texto tem algo diferente disso
	for car in texto:
		if car < 'a' or car > 'z':
			return 0
	return 1

def so_az_etc(texto, etc):
	# retorna 1 se texto só tem letras de 'a' a 'z' (minusculas) e etc.
	# retorna 0 se texto tem algo diferente disso
	for car in texto:
		if car < 'a' or car > 'z':
			if not car in etc: return 0
	return 1

def multi_split(texto, seps):
	lt_nova = []
	item = ''
	for car in texto:
		if car in seps: 
			if item:
				lt_nova.append(item)
				item = ''
		else:
			item = item + car
	if item: lt_nova.append(item)
	return lt_nova	
	
def digi_split(texto):
	DIGI = '0123456789'
	# separa partes numéricas e não numéricas do texto
	lt_nova = []
	item = ''
	digi_flag = 0
	for car in texto:
		if digi_flag:
			if car in DIGI:
				item = item + car
			else:
				if item:
					lt_nova.append(item)
				item = car
				digi_flag = 0
		else:
			if car in DIGI:
				if item:
					lt_nova.append(item)
				item = car
				digi_flag = 1
			else:
				item = item + car
	if item: lt_nova.append(item)
	return lt_nova	

def split_termo(termo, lt_vazias=None):
	termo = strip(termo)
	termo = cars2ascii(termo)
	termo = lower(termo)
	termo = RE_TAG.sub('', termo)
	termo = replace(termo, '(', ' ')
	termo = replace(termo, ')', ' ')
	if len(termo) and termo[-1] == ':': termo = termo[:-1]
	lt_termo = split(termo)
	# remover palavras vazias, exceto se for a primeira
	if lt_vazias:
		lt_termo = lt_termo[:1] + remover_vazias(lt_termo[1:], lt_vazias)
	lt_termo = remover_duplicatas(lt_termo)
	
	tipo = None
	if len(lt_termo) == 1:
		termo = lt_termo[0]
		if so_az(termo): 
			tipo = TIPO_SIMPLES
		elif so_az_etc(termo, '-'):
			tipo = TIPO_HIFEN
		else: 
			tipo = TIPO_SIMBOLO
	else: 
		tipo = TIPO_LOCUCAO
			

	lt_nova = []
	for parte in lt_termo:
		lt_parte = multi_split(parte, SEPARADORES)
		lt_nova = lt_nova + lt_parte
	lt_termo = lt_nova	

	lt_nova = []
	for parte in lt_termo:
		lt_parte = digi_split(parte)
		lt_nova = lt_nova + lt_parte
	lt_termo = lt_nova	

	lt_termo = remover_duplicatas(lt_termo)

	return tipo, lt_termo		
