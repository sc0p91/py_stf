#!/usr/bin/python3.7

import os, glob, json, shutil

try:
    os.mkdir('receipts/processed')
except OSError:
    print("Directory already exists")

receipts = glob.glob('./receipts/new/receipt-[0-9]*.json')
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split("/")[-1]
    destination = f"./receipts/processed/{name}"
    shutil.move(path, destination)
    print (f"moved '{path}' to '{destination}'")

print ("Receipt subtotal: $%.2f" % subtotal)
