#!/python/python
# ref_idx.py - dicionário open-source - índice de referências

print 'Content-type: text/html\n'

try:
	import cgi
	import ODBC.Windows
	#from hx_latin1 import cars2ascii
	from string import strip
	
	DSN = 'kayak_mysql_lexicomp'
	
	print "<HTML><HEAD><TITLE>Índice de Referências</TITLE>"

	obs = ''
	form = cgi.FieldStorage()
	termo_form = ''
	dados = None
	if form.has_key('termo_form'):
		termo_form = form['termo_form'].value
	else:
		termo_form = ''
		
	print """</HEAD><BODY>
	<FORM action="#form"><A NAME="form">
	<INPUT TYPE="text" NAME="termo_form" VALUE="%s">
	<INPUT TYPE="submit" NAME="bt_ok_form" VALUE="Buscar">
	</FORM><HR>""" % (termo_form) 
	
	conexao = None
	if termo_form:
		sql = """SELECT i.id_ref, r.term_en, r.term_pt
				 FROM i_referencia as i, referencia as r
				 WHERE i.id_ref = r.id_ref
				 AND i.term_az = "%s" 
				 ORDER BY i.id_ref"""
		conexao = ODBC.Windows.Connect(dsn=DSN,clear_auto_commit=0)
		cursor = conexao.cursor()
		cursor.execute(sql % termo_form)
		dados = cursor.fetchall()
		if dados:
			print '<TABLE BORDER=1 WIDTH="35%"><TR><TH WIDTH="60">REF<TH>Termo</TR>'
			for id_ref, term_en, term_pt in dados:
				if term_pt: term_pt = ' <FONT COLOR="green">%s</FONT>' % term_pt
				else: term_pt = ''
				print '<TR><TD VALIGN="top"><A HREF="#form?id_ref_form=%s">%s</A><TD VALIGN="top">%s %s</TR>' % (
					id_ref, id_ref, term_en, term_pt)
			print '</TABLE>'
			
	if form.has_key('id_ref_form'):
		id_ref_form = form['id_ref_form'].value
	else:
		id_ref_form = ''
	if id_ref_form:
		if not conexao:
			conexao = ODBC.Windows.Connect(dsn=DSN,clear_auto_commit=0)
			cursor = conexao.cursor()
		sql = """SELECT term_en, term_pt, defin 
				 FROM referencia
				 WHERE id_ref = "%s" """
		cursor.execute(sql % termo_form)
		dados = cursor.fetchall()
		if dados:
			for id_ref, term_en, term_pt in dados:
				print """
<TABLE BORDER=1 WIDTH="100%">
<TR><TH>EN<TD>%s</TR>
<TR><TH><FONT COLOR="green">PT</FONT><TD><FONT COLOR="green">%s</FONT></TR>
<TR><TD COLSPAN=2>%s</TR>
</TABLE>""" % (term_en, term_pt, defin)

	print '<HR>', cgi.print_environ()
  
except:
	import sys
	from traceback import print_exc
	sys.stderr = sys.stdout
	print '<HR><H3>Erro no CGI:</H3><PRE>'
	print_exc()
	print '</PRE>'

print '</BODY></HTML>'