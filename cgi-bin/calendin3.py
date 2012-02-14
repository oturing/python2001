#!/python/python
# calendin.py - calendário dinâmico - protótipo 2

print 'Content-type: text/html\n'

try:
    import cgi
    from time import time, localtime
    from calendar import monthcalendar
    from string import join
    
    obs = ''
    form = cgi.FieldStorage()
    ano = mes = None
    if form.has_key('ano') and form.has_key('mes'):
        try:
            ano = int(form['ano'].value)
            mes = int(form['mes'].value)
            if not ano in range(1970, 2038):
                obs = 'Somente anos de 1970 a 2037 podem ser consultados.'
                raise ValueError
        except ValueError:
            ano = None            
            
    if not ano:
        ano, mes = localtime(time())[:2]
        
    mes_ant = mes - 1
    if mes_ant == 0:
        mes_ant = 12
        ano_ant = ano - 1
    else:
        ano_ant = ano
    
    mes_seg = mes + 1
    if mes_seg == 13:
        mes_seg = 1
        ano_seg = ano + 1
    else:
        ano_seg = ano

    print '<HTML><TITLE>Calendário Dinâmico</TITLE>'
    print '<BODY>'

    print '<H1>Calendário do mês %02d/%04d</H1>' % (mes, ano)
    print '<TABLE>'
    print '<TR>'
    for dia_sem in ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']:
        if dia_sem == 'sab' or dia_sem == 'dom':
            bgcolor = 'BGCOLOR="green"'
        else:
            bgcolor = 'BGCOLOR="blue"'
        print '<TH WIDTH="35" %s><H3>%s</H3></TH>' % (bgcolor, dia_sem)
    print '</TR>'    
    for semana in monthcalendar(ano, mes):
        print '<TR>'
        num_dia_sem = 0
        for dia in semana:
            if num_dia_sem >= 5:
                bgcolor = 'BGCOLOR="lightgreen"'
            else:
                bgcolor = 'BGCOLOR="lightblue"'
            print '<TD ALIGN="RIGHT" %s>' % bgcolor
            if dia != 0: 
                print '<H2>%2d</H2>' % dia
            print '</TD>'
            num_dia_sem = num_dia_sem + 1
        print '</TR>'
    print '<CAPTION>'
    print '<A HREF="?ano=%s&mes=%s">mês anterior</A>' % (ano_ant, mes_ant)
    print '&nbsp;|&nbsp;'
    print '<A HREF="?ano=%s&mes=%s">mês seguinte</A>' % (ano_seg, mes_seg)
    print '</CAPTION>'
    print '</TABLE>'
    print '<P>%s</P>' % obs

except:
    import sys
    from traceback import print_exc
    sys.stderr = sys.stdout
    print '<HR><H3>Erro no CGI:</H3><PRE>'
    print_exc()
    print '</PRE>'

print '</BODY></HTML>'