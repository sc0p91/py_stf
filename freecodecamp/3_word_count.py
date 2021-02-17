#!/usr/bin/python3
import os

ipstr = input("Let me count some words! [file,str] ")

if os.path.exists(ipstr):
    if os.path.isdir(ipstr):
        print(f"{ipstr} is a dir... can't do anything with that")
    else:
        with open(ipstr) as f:
            sum = f.read().split()
else:
    sum = ipstr.split()

print(f"{len(sum)} words found.")
