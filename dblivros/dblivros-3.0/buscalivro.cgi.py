#! /usr/bin/python2
# procura um livro baseado em argumentos da linha de comando

print 'Content-type: text/plain'
print

home = '/home/lalo/src/hiper/dblivros/'

import sys
sys.path.append(home)
from livros import livro
from dblivros import db, abrir
livros = abrir(home + 'dblivros.pickle')

import cgi
form = cgi.FieldStorage()
if form.has_key('expr'):
    criterio = form['expr'].value
else:
    criterios = []
    if form.has_key('titulo'):
        criterios.append('l.titulo == %s' % `form['titulo'].value`)
    if form.has_key('autor'):
        criterios.append('%s in l.autores' % `form['autor'].value`)
    if form.has_key('isbn'):
        criterios.append('l.isbn == %s' % `form['isbn'].value`)
    if form.has_key('editora'):
        criterios.append('l.editora == %s' % `form['editora'].value`)
    if form.has_key('paginas_min'):
        criterios.append('l.paginas >= %s' % form['paginas_min'].value)
    if form.has_key('paginas_max'):
        criterios.append('l.paginas <= %s' % form['paginas_max'].value)
    if form.has_key('preco_min'):
        criterios.append('l.preco >= %s' % form['preco_min'].value)
    if form.has_key('preco_max'):
        criterios.append('l.preco <= %s' % form['preco_max'].value)
    criterio = ' and '.join(criterios) or 'l.isbn'

if form.has_key('debug'):
    print 'Express\343o utilizada:', `criterio`
    print

res = livros.busca(criterio)
if res:
    for l in res:
        l.exibir()
else:
    print 'Nenhum livro cadastrado atende os crit\351rios'
