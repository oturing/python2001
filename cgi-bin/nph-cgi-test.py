#!/python/python

import sys
import traceback
import cgi 
from os import environ
from time import sleep

print '%s 200 OK' %  environ['SERVER_PROTOCOL']
print 'Server: %s' %  environ['SERVER_SOFTWARE']
print "Content-type: text/plain"
print
sys.stderr = sys.stdout
try:
	print 'Contagem regressiva:'
	print
	for i in range(10):
		print 11-i
		sleep(1)
	print 
	print 'Fogo!'
except:
	print "\n\n"
	traceback.print_exc()