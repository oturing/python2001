#!/python/python
# ref_idx.py - dicionário open-source - índice de referências

print 'Content-type: text/html\n'

try:
	import cgi
	import ODBC.Windows
	from dic_util import split_termo
	from string import strip, join
	
	DSN = 'kayak_mysql_lexicomp'
	
	print "<HTML><HEAD><TITLE>Índice de Referências</TITLE>"

	obs = ''
	form = cgi.FieldStorage()
	termo_form = ''
	lt_termo = []
	dados = None
	if form.has_key('termo_form'):
		termo_form = form['termo_form'].value
		tipo, lt_termo = split_termo(termo_form)
		termo_form = join(lt_termo)
	else:
		termo_form = ''
		
	print """</HEAD><BODY><TABLE BORDER=0 BGCOLOR="#FF9999" WIDTH="100%"><TR><TD VALIGN="middle">"""
	print """<FORM action="ref_idx.py"><A NAME="form">
	<INPUT TYPE="text" NAME="termo_form" VALUE="%s" SIZE="30">
	<INPUT TYPE="submit" NAME="bt_ok_form" VALUE="Buscar">
	</FORM></TR></TABLE>""" % (termo_form) 
	
	conexao = None
	if termo_form:
		sql = """SELECT DISTINCT i.id_ref, r.term_en, r.term_pt
				 FROM i_referencia as i, referencia as r
				 WHERE i.id_ref = r.id_ref
				 AND i.term_az = "%s" 
				 ORDER BY i.id_ref"""
		conexao = ODBC.Windows.Connect(dsn=DSN,clear_auto_commit=0)
		cursor = conexao.cursor()
		cursor.execute(sql % termo_form)
		dados = cursor.fetchall()
		if dados:
			print '<TABLE BORDER=0 BGCOLOR="#CCCCFF" WIDTH="35%" ALIGN="left">'
			for id_ref, term_en, term_pt in dados:
				if term_pt: term_pt = ' <FONT COLOR="green">%s</FONT>' % term_pt
				else: term_pt = ''
				print '<TR><TD VALIGN="top" WIDTH=60><A HREF="ref_idx.py?termo_form=%s&id_ref_form=%s">%s</A><TD VALIGN="top">%s %s</TR>' % (
					termo_form, id_ref, id_ref, term_en, term_pt)
			print '</TABLE>'
			
	if form.has_key('id_ref_form'):
		id_ref_form = form['id_ref_form'].value
	elif len(dados) == 1: #só há uma resposta; vamos exibir
		id_ref_form = id_ref
	else:
		id_ref_form = ''
	if id_ref_form:
		if not conexao:
			conexao = ODBC.Windows.Connect(dsn=DSN,clear_auto_commit=0)
			cursor = conexao.cursor()
		sql = """SELECT term_en, term_pt, glos 
				 FROM referencia
				 WHERE id_ref = "%s" """
		cursor.execute(sql % id_ref_form)
		dados = cursor.fetchall()
		if dados:
			for term_en, term_pt, glos in dados:
				print """<TABLE BORDER=0 BGCOLOR="#FFFFCC" WIDTH="65%" ALIGN="right">"""
				if strip(term_en): 
					print """<TR><TH WIDTH="10" BGCOLOR="#FFFF66">EN<TD>%s</TR>""" % term_en
				if strip(term_pt): 
					print """<TR><TH WIDTH="10" BGCOLOR="#FFFF66"><FONT COLOR="green">PT</FONT>"""
					print """<TD BGCOLOR="#FFFFCC"><FONT COLOR="green">%s</FONT></TR>""" % term_pt
					
				print """<TR><TD COLSPAN=2>%s [%s]</TR></TABLE>""" % (glos, id_ref_form)

	#print '<HR>', cgi.print_environ()
  
except:
	import sys
	from traceback import print_exc
	sys.stderr = sys.stdout
	print '<HR><H3>Erro no CGI:</H3><PRE>'
	print_exc()
	print '</PRE>'

print '</BODY></HTML>'