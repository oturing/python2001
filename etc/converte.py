#!/usr/bin/env python
from pprint import pprint
lista = open("/jobs/curso/deputados.tab").readlines()
lista = [ x.split('\t') for x in lista ]
lista = [ x[0:2] + [x[3]] for x in lista ]
lista = [ '\t'.join([' '.join(x[0].split()[:-1]),
                     x[0].split()[-1],
                     'D' + x[1][1:], x[2]]) + '\n'
          for x in lista ]
print '\n'.join(lista[:5])
open("/jobs/curso/funcionarios.tab","w").writelines(lista)
