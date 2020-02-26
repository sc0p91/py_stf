#!/usr/bin/python3.7

import sys, os

fcontent = ""

fname = input("Enter Filename: ")

if os.path.exists(fname):
    print(f"File \"{fname}\" already exsists")
    exit(1)

print("Now enter Content.")
print("When you're finished,")
print("enter an empty line")
print("or a single full stop")

while True:
    readline = input("- ")
    if readline and readline != '.':
        fcontent = fcontent + readline + "\n"
    else:
        break

if fname and fcontent:
    try:
        with open(f'./{fname}', 'w') as f:
            f.write(f"{fcontent}\n")
            print(f"File \"{fname}\" has been written.")
    except:
        e = sys.exc_info()[0]
        print(f"Error! {e}")
else:
    print("Please provide a Filename & Filecontent")
