#!/python/python

import sys
import traceback
import cgi 

NUM_LINS = 9
NUM_COLS = 12
COLS = map(lambda col: chr(ord('A')+col), range(NUM_COLS))
LINS = range(1,NUM_LINS+1)

print "Content-type: text/html"
print
sys.stderr = sys.stdout
try:
	print '<h2>Takeover</h2>'
	print '<table border=1>'
	for lin in LINS:
		print '<tr>'
		for col in COLS:
			cel = '%s%s' % (col,lin)
			print '<td width="32" height="32" align="center" valign="middle">%s</td>' % cel
		print '</tr>'
	print 
	print '</table>'
except:
	print "\n\n"
	traceback.print_exc()