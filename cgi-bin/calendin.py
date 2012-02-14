#!/python/python
# calendin.py - calendário dinâmico - protótipo 1

print 'Content-type: text/html\n'

try:
    from time import time, localtime
    from calendar import monthcalendar
    from string import join

    ano, mes = localtime(time())[:2]
    
    print '<HTML><TITLE>Calendário Dinâmico</TITLE>'
    print '<BODY>'

    print '<H1>Calendário do mês %02d/%04d</H1>' % (mes, ano)
    print '<PRE>'
    for semana in monthcalendar(ano, mes):
        print join( map(str, semana),'\t' )
    print '</PRE>'

except:
    import sys
    from traceback import print_exc
    sys.stderr = sys.stdout
    print '<HR><H3>Erro no CGI:</H3><PRE>'
    print_exc()
    print '</PRE>'

print '</BODY></HTML>'