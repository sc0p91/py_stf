#!/usr/bin/python3.7

import os, math

try:
    digs = int(os.getenv("DIGITS", default=10))
except:
    print("No valid input defined")
    exit(1)

print("%.*f" % (digs, math.pi))
