#!/python/python
from time import time

print 'Content-type: text/html'
print
print '<HTML><BODY>'
print '<H1>Hora certa*: %s</H1>' % localtime(time())
print '<P>* de acordo com o relógio interno deste servidor</P>'
print '</BODY></HTML>'
