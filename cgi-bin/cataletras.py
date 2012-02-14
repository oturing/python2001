#!/python/python

import cgi
import sys
import traceback
from string import split, join, strip

sep = '\n'

print "Content-type: text/html"
print
sys.stderr = sys.stdout
try:
    print '<H1>Cataletras</H1>'
    form = cgi.FieldStorage()
    if form.has_key('PALAVRA'):
        palavra = form['PALAVRA'].value
        palavra = strip(palavra)
    else:
        palavra = ''
    if form.has_key('LISTA'):
        lista = split(form['LISTA'].value, sep)
        print '<BR>LISTA: ' + `lista`
    else:
        lista = []
    if palavra:
        print '<H2>%s</H2>' % palavra
        lista.append(strip(palavra))
    else:
        lista = []
    print '<FORM ACTION="cataletras.py" METHOD="GET">'
    print '<INPUT TYPE="TEXT" NAME="PALAVRA">'
    print '<INPUT TYPE="HIDDEN" NAME="LISTA" VALUE="%s">' % join(lista, sep)
    print '<INPUT TYPE="SUBMIT" VALUE="Enviar">'
    print '<INPUT TYPE="SUBMIT" VALUE="Limpar">'
    print '</FORM>'
    if lista:
        print '<PRE>%s</PRE>' % join(lista, sep)
except:
    print "\n\n<PRE>"
    traceback.print_exc()