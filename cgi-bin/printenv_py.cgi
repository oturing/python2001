#!/usr/local/bin/python

from os import environ

print "Content-type: text/html\n"
for ( key, val ) in environ.items():
    print "%s = %s<BR>" % ( key, val )


