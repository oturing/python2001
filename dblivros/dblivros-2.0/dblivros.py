from livros import livro

def upgrade(lista):
    res = []
    for l in lista:
        res.append(livro(l['Titulo'], l['Autores'], l['ISBN'],
                         l['Editora'], l['Preco'], l['Paginas']))
    return res

from dbsimples import db

def abrir(nome='dblivros.pickle'):
    livros = db(nome)
    if len(livros.lista) and type(livros.lista[0]) == type({}):
        livros.lista = upgrade(livros.lista)
    return livros

livros = abrir()

if __name__ == '__main__':
    livros.salva()
    for item in livros.lista:
        item.exibir()
