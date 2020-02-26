#!/usr/bin/python3.7

import sys, os

fcontent = ""

fname = input("Enter File to read: ")

# Test if the file exists
try:
  f = open(fname)
except FileNotFoundError as err:
  print(err)
  sys.exit(1)
else:
  try:
    fline = int(input("Enter Linenumber to read: "))-1
  except:
    print("Can't parse input")
  with f:
    lines = f.readlines()
    if len(lines) > fline:
        print(lines[int(fline)])
    else:
        print(f"{fname} doesn't have {fline} lines ({len(lines)+1})")
