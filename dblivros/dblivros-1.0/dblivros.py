import pickle

nome_default = 'dblivros.pickle'

def abrir(nome=nome_default):
    return pickle.load(open(nome))

lista = abrir()

def busca(condicao="l", lista=lista):
    res = []
    for l in lista:
	if eval(condicao):
	    res.append(l)
    return res

def salva(lista=lista, nome_default=nome_default):
    pickle.dump(lista, open(nome_default, 'w'))

if __name__ == '__main__':
    for item in lista:
        print item
