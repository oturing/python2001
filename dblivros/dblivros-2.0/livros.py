class livro:
    def __init__(self, titulo='', autores=(), isbn='', editora='',
                 preco=0.0, paginas=0):
        self.titulo = titulo
        self.autores = autores
        self.isbn = isbn
        self.editora = editora
        self.preco = preco
        self.paginas = paginas

    def exibir(self):
        print self.titulo, ' '*10, ', '.join(self.autores)
        print '  Editora: %s   ISBN: %s' % (self.editora, self.isbn)
        print '  Pre\347o: US$ %5.2f   (%d P\341ginas)' % (self.preco, self.paginas)

