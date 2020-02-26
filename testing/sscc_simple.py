#!/usr/bin/python

import sys


# SIMPLE VERSION
if len(sys.argv) == 1:
    print 'GIEV ARGS'
else:
    print 'Amount Args: ', len(sys.argv[1:])
    print 'Content Args: ', str(sys.argv[1:])
