import pickle

class db:
    def __init__(self, nome='db.pickle'):
        self.nome = nome
        try:
            self.lista = pickle.load(open(nome))
        except IOError:
            self.lista = []

    def busca(self, condicao="l",):
        res = []
        for l in self.lista:
            if eval(condicao):
                res.append(l)
        return res

    def salva(self, nome=None):
        pickle.dump(self.lista, open(nome or self.nome, 'w'))

if __name__ == '__main__':
    dados = db()
    for item in dados.lista:
        print item
