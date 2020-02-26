#!/usr/bin/python3.7

import os, glob, json, shutil, re, math

try:
    os.mkdir('receipts/processed')
except OSError:
    print("Directory already exists")

# Process all the files
# receipts = glob.glob('./receipts/new/receipt-[0-9]*.json')
# Only process even files:
receipts = [ f for f in glob.iglob('receipts/new/receipt-[0-9]*.json') if re.match('receipts/new/receipt-[0-9]*[24680].json', f) ]
subtotal = 0.0

# No need to get the whole list into the memory
#for path in receipts:
for path in glob.iglob('receipts/new/receipt-[0-9]*.json'):
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    # Doesnt need to be done with 2 lines
    #name = path.split("/")[-1]
    #destination = f"./receipts/processed/{name}"
    destination = path.replace('new','processed')
    shutil.move(path, destination)
    print (f"moved '{path}' to '{destination}'")

# Better use math to create a more readable statement
#print ("Receipt subtotal: $%.2f" % subtotal)
print (f"Receipt subtotal: ${subtotal}")
print (f"Receipt subtotal: ${math.ceil(subtotal)}")
print (f"Receipt subtotal: ${math.floor(subtotal)}")
print (f"Receipt subtotal: ${round(subtotal, 2)}")
