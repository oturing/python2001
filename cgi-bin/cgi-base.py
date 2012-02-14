#!/python/python

import sys
import traceback
print "Content-type: text/html"
print
sys.stderr = sys.stdout
try:
    print '<H1>Palavras</H1>'
    print '<TABLE BORDER=1>'
except:
    print "\n\n<PRE>"
    traceback.print_exc()