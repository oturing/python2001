#!/python/python
# ref_idx.py - dicionário open-source - índice de referências

print 'Content-type: text/html\n'

try:
	import cgi
	import ODBC.Windows
	#from hx_latin1 import cars2ascii
	from string import strip
	
	print "<HTML><HEAD><TITLE>Índice de Referências</TITLE>"

	obs = ''
	form = cgi.FieldStorage()
	termo_form = ''
	dados = None
	if form.has_key('termo_form'):
		termo_form = form['termo_form'].value
		print """</HEAD><BODY>
		<FORM action="ref_idx.py">
		<INPUT TYPE="text" NAME="termo_form" VALUE="%s">
		<INPUT TYPE="submit" NAME="bt_ok_form" VALUE="Buscar">
		</FORM><HR>""" % (termo_form) 

		sql = """SELECT i.id_ref, r.term_en, r.term_pt
				 FROM i_referencia as i, referencia as r
				 WHERE i.id_ref = r.id_ref
				 AND i.term_az = "%s" """
		conexao = ODBC.Windows.Connect(dsn='kayak_mysql_lexicomp',clear_auto_commit=0)
		cursor = conexao.cursor()
		res = cursor.execute(sql % termo_form)
		dados = cursor.fetchall()
		if dados:
			print '<TABLE BORDER=1><TR><TH>REF<TH>Termo</TR>'
			for id_ref, term_en, term_pt in dados:
				if term_pt: term_pt = ' <FONT COLOR="red">%s</FONT>' % term_pt
				else: term_pt = ''
				print '<TR><TD><A HREF="ref_idx.py?id_ref=%s">%s</A><TD>%s %s</TR>' % (
					id_ref, id_ref, term_en, term_pt)
			print '</TABLE>'

  
except:
	import sys
	from traceback import print_exc
	sys.stderr = sys.stdout
	print '<HR><H3>Erro no CGI:</H3><PRE>'
	print_exc()
	print '</PRE>'

print '</BODY></HTML>'