#!/python/python
# hora.py - CGI que exibe a hora local do servidor

from time import time, localtime

print 'Content-type: text/html'
print

h, m, s = localtime(time())[3:6]
print '<HTML><BODY>'
print '<H1>Hora: %02d:%02d:%02d</H1>' % (h, m, s)
print '<P>* de acordo com o relógio interno deste servidor</P>'
print '</BODY></HTML>'