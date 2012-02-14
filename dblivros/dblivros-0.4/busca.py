def busca(lista, condicao):
    res = []
    for l in lista:
	if eval(condicao):
	    res.append(l)
    return res

