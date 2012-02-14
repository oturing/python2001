#example writen by GvR
#zope course
#herndon va
#31/jan/2002

#almost everything that is succesful in python was stolen from other languages

#pure luck is what makes a language succesful

from __future__ import generators

def fibo(a, b):
    while 1:
        yield a
        a, b = a + b, a

t = fibo(1, 1)
t.next()
t.next()
for x in t:
    print x
