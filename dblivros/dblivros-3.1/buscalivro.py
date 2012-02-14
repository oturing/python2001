#! /usr/bin/python2
# procura um livro baseado em argumentos da linha de comando

from dblivros import *
import sys

res = livros.busca(' and '.join(sys.argv[1:]) or 'l.isbn')
if res:
    for l in res:
        l.exibir()
else:
    print 'Nenhum livro cadastrado atende os crit\351rios'
