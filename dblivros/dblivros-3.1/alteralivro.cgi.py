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
if not form.has_key('isbn_o'):
    print 'Para alterar um livro, forneça o isbn'
    sys.exit(1)

res = livros.busca('l.isbn == %s' % `form['isbn_o'].value`)
if res:
    for l in res:
	print 'alterando:'
	l.exibir()
	if form.has_key('titulo'):                                         
	    l.titulo = form['titulo'].value
	if form.has_key('autor'):
	    l.autor = form['autor'].value.splitlines()
	if form.has_key('isbn'):                                               
	    l.isbn = form['isbn'].value
	if form.has_key('editora'):                                            
	    l.editora = form['editora'].value
	if form.has_key('paginas'):
	    l.paginas = int(form['paginas'].value)
	if form.has_key('preco'):
	    l.preco = float(form['preco'].value)
	print 'para:'
	l.exibir()
    livros.salva()
else:
    print 'Nenhum livro cadastrado atende os crit\351rios'
