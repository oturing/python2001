#!/python/python
# uma maquina de somar via CGI
# exibe formulário com um campo que quando preenchido e submetido 
# é somado a um total

from string import join, split
import os
import operator

print 'Content-type: text/html\n'

try:
	import cgi
	form = cgi.FieldStorage()
	lista_nums = []
	total = 0

	print '<HTML><TITLE>CGI Somador</TITLE>'
	print '<BODY>'
	print '<H1>Somador</H1>'

	if form.has_key('lista_nums'):
		lista_nums = map(float, split(form['lista_nums'].value))

	if form.has_key('parcela'):
		lista_nums.append(float(form['parcela'].value))

	if lista_nums:
		total = reduce(operator.add, lista_nums)

	print '<TABLE BORDER=1>'
	print '<TR>'
	print '<TD ALIGN="RIGHT">'
	for num in lista_nums:
		print '%0.2f<BR>' % num
	print '</TD></TR>'
	print '<TR><TH ALIGN="LEFT">%0.2f</TH></TR>' % total
	print '<TR>'
	print '<TD ALIGN="RIGHT">'
	print '<FORM ACTION="%s" METHOD="GET">' % os.environ['SCRIPT_NAME']
	print '<INPUT TYPE="TEXT" NAME="parcela">'
	if lista_nums:
		print '<INPUT TYPE="HIDDEN" NAME="lista_nums" VALUE="%s">' % join(map(str, lista_nums))
	print '<INPUT TYPE="SUBMIT" VALUE="+">'
	print '</FORM>'
	print '</TD></TR>'

	print '</TABLE>'
	
	#print cgi.test()

except:
	import sys
	from traceback import print_exc
	sys.stderr = sys.stdout
	print '</TABLE><HR><H3>Erro no CGI:</H3><PRE>'
	print_exc()
	print '</PRE><HR>'

print '</BODY></HTML>'