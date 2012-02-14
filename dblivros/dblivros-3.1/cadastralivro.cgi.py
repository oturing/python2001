#!/usr/bin/python2
# procura um livro baseado em argumentos da linha de comando

print 'Content-type: text/plain'
print

def falha(mensagem):
    print mensagem
    sys.exit(0)

home = '/var/www/dblivros/'

import sys
sys.path.append(home)
from livros import livro
from dblivros import db, abrir
livros = abrir(home + 'dblivros.pickle')

import cgi
form = cgi.FieldStorage()
if not form.has_key('titulo'):                                         
    falha('Campo não fornecido: titulo')
if not form.has_key('autor'):
    falha('Campo não fornecido: autor')
if not form.has_key('isbn'):                                               
    falha('Campo não fornecido: isbn')
if not form.has_key('editora'):                                            
    falha('Campo não fornecido: editora')
if not form.has_key('paginas'):
    falha('Campo não fornecido: paginas')
if not form.has_key('preco'):
    falha('Campo não fornecido: preco')

print 'inserindo:'
l = livro(form['titulo'].value, form['autor'].value.splitlines(),
          form['isbn'].value, form['editora'].value,
	  float(form['preco'].value), int(form['paginas'].value))
l.exibir()
livros.lista.append(l)
livros.salva()
print 'ok'
