#!/usr/bin/env python

from time import gmtime, strftime

s_final = 2**31

for i in range(9,-1,-1):
    s = s_final-i
    t = gmtime(s)
    print '2**31-%s --> %s' % (i, t)
    
print
print 'data maxima:', strftime('%Y-%m-%d %H:%M:%S UTC', gmtime(2**31-1))
    
