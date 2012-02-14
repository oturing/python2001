#!/usr/bin/env python

'''
Jeremias, o programador repentista

'''

from random import choice

class LiqLit:
    def __init__(self, texto, tam_frag=3):
        self.texto = texto
        self.tam_frag = tam_frag    #tamanho do fragmento
        self.tabela = self._montar_tabela()

    def _montar_tabela(self):
        pos = 0
        tab = {}
        texto = ' ' + self.texto 
        # coloco este espaço para permitir que o trecho inicial possa aparecer
        # como continuação, após qualquer outro espaço existente no texto
        # e também como trecho inicial selecionado pelo método bater
        while (pos + self.tam_frag) <= len(self.texto):
            frag = self.texto[pos:pos+self.tam_frag]
            ocor = tab.setdefault(frag,[])
            try:
                ocor.append(self.texto[pos + self.tam_frag])
            except IndexError:
                #no caso especial do ultimo fragmento
                #colocamos um espaço em branco
                ocor.append(' ')
            pos += 1
        return tab
        
    def _selecionar_trecho_inicial(self):
        candidatos = []
        todos_os_trechos = self.tabela.keys()
        for trecho in todos_os_trechos:
            if trecho[0].isupper():
                candidatos.append(trecho)
        if not candidatos:
            for trecho in todos_os_trechos:
                if trecho[0] == ' ':
                    candidatos.append(trecho)
        if not candidatos:
            canditados = todos_os_trechos
        return choice(candidatos)
        
    def bater(self):
        trecho = self._selecionar_trecho_inicial()
        batido = [trecho]
        prox_car = None
        while len(batido) < len(self.texto) or prox_car != ' ':
            try:
                prox_car = choice(self.tabela[trecho])
            except KeyError: #TODO: sequencia final???
                break    
            batido.append(prox_car)
            trecho = trecho[1:] + prox_car
        batido = ''.join(batido)
        return batido.strip()   
    
def teste_tabela(texto):
    liq = LiqLit(texto, 2)
    tabela = liq.tabela.items()
    tabela.sort()
    for trecho, lista in tabela:
        print trecho, lista
        
def teste_bater(texto, vezes):
    liq = LiqLit(texto, 4)
    for i in xrange(vezes):
        print liq.bater()
        print '-' * 60
        
def teste_bater2(nome_arq, tam_frag):
    texto = open(nome_arq).read()
    liq = LiqLit(texto, tam_frag)
    print '%s (tam_frag=%s)' % (nome_arq, tam_frag)
    print '-' * 60
    print liq.bater()
    
if __name__=='__main__':
    texto = 'Batatinha quando nasce esparrama pelo chão, o menino quando dorme faz pipi no colchão.'
    #teste_tabela(texto)  
    #teste_bater(texto, 20)
    
    teste_bater2('critica-arte-00.txt', 6) 
    
    
'''TODO: resolver melhor este este caso:
Traceback (most recent call last):
  File "./LiqLit.py", line 52, in ?
    teste_bater(texto)  
  File "./LiqLit.py", line 47, in teste_bater
    print liq.bater()
  File "./LiqLit.py", line 31, in bater
    prox_car = choice(self.tabela[trecho])
KeyError: . 

Traceback (most recent call last):
  File "./LiqLit.py", line 88, in ?
    teste_bater2('critica-arte-01.txt', 4) 
  File "./LiqLit.py", line 81, in teste_bater2
    print liq.bater()
  File "./LiqLit.py", line 50, in bater
    trecho = self._selecionar_trecho_inicial()
  File "./LiqLit.py", line 47, in _selecionar_trecho_inicial
    return choice(candidatos)
  File "/usr/lib/python2.2/random.py", line 328, in choice
    return seq[int(self.random() * len(seq))]
IndexError: list index out of range

'''     