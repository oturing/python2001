#!/python/python
# calendin.py - calendário dinâmico - protótipo 2

print 'Content-type: text/html\n'

try:
    from time import time, localtime
    from calendar import monthcalendar
    from string import join

    ano, mes, hoje = localtime(time())[:3]
    
    print '<HTML><TITLE>Calendário Dinâmico</TITLE>'
    print '<BODY>'
    print '<CENTER>'
    print '<H1>Calendário de %02d/%04d</H1>' % (mes, ano)
    print '<TABLE>'
    print '<TR>'
    for dia_sem in ['seg','ter','qua','qui','sex','sab','dom']:
        if dia_sem in ['sab','dom']: bgcolor = 'green'
        else: bgcolor = 'blue'
        print '<TH WIDTH="45" BGCOLOR="%s">' % bgcolor
        print '<H3>%s</H3></TH>' % dia_sem
    print '</TR>'    
    for semana in monthcalendar(ano, mes):
        print '<TR>'
        num_dia_sem = 0
        for dia in semana:
            if dia == hoje: 
                bgcolor = 'pink'
            elif num_dia_sem >= 5:
                bgcolor = 'lightgreen'
            else:
                bgcolor = 'lightblue'
            print '<TD ALIGN="RIGHT" BGCOLOR="%s">' % bgcolor
            if dia != 0: 
                print '<H2>%2d</H2>' % dia
            print '</TD>'
            num_dia_sem = num_dia_sem + 1
        print '</TR>'    
    print '</TABLE></CENTER>'

except:
    import sys
    from traceback import print_exc
    sys.stderr = sys.stdout
    print '<HR><H3>Erro no CGI:</H3><PRE>'
    print_exc()
    print '</PRE>'

print '</BODY></HTML>'