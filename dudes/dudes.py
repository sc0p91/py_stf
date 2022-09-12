#!/usr/bin/python3

#!/usr/bin/python3
import sys
import random

# Vars
i = 0
anz = 300
dudes=[]
generator=True
hats = ['Fedora', 'Tophat', 'Cap', 'Woolhat']
colr = ['red', 'blue', 'black', 'green', 'yellow', 'white', 'orange']
shrt = ['Shirt', 'Tanktop', 'Pullover', 'Hoodie']
smok = ['Cigarette', 'Cigar', 'Pipe']

# Functions
def randomizer(item):
    rand = random.randint(0,len(item)-1)
    item = item[rand]
    return item

while generator:
    dude = (randomizer(colr),randomizer(hats),randomizer(colr),randomizer(shrt),randomizer(smok))
    i += 1
    if dude not in dudes:
        dudes.append(dude)
        if len(dudes) == anz:
            print("Do si {} ungerschidlechi dudes: {}".format(anz,dudes))
            generator=False

print ("Und es het nume {} Iteratione brucht :)".format(i))
