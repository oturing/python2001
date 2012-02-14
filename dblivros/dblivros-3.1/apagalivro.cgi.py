#!/usr/bin/python2
# procura um livro baseado em argumentos da linha de comando

print 'Content-type: text/plain'
print

home = '/var/www/dblivros/'

import sys
sys.path.append(home)
from livros import livro
from dblivros import db, abrir
livros = abrir(home + 'dblivros.pickle')

import cgi
form = cgi.FieldStorage()
if not form.has_key('isbn'):                                               
    falha('Para apagar um livro, forneça o isbn')

res = livros.busca('l.isbn == %s' % `form['isbn'].value`)
if res:
    for l in res:
	print 'removendo:'
	l.exibir()
        livros.lista.remove(l)
    livros.salva()
else:
    print 'Nenhum livro cadastrado atende os crit\351rios'
