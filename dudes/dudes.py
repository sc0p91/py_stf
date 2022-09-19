#!/usr/bin/python3
import sys
import numpy as np
from PIL import Image

# Vars
i = 0
anz = 500
dudes = []
generator = True
head = Image.open("img/head.png")

#hats = ['none', 'Fedora', 'Tophat', 'Cap', 'Woolhat']
hats = ['none', 'Fedora', 'Tophat', 'Cap', 'Woolhat']
colr = ['green', 'blue', 'black', 'orange', 'yellow', 'white', 'red']
shrt = ['Shirt', 'Tanktop', 'Pullover', 'Hoodie']
smok = ['none', 'Pipe', 'Cigar', 'Cigarette']

# Functions
def randomizer():
    workdude=[]

    # Setup the Hat Image
    ht = np.random.choice(hats, size=1, p=[0.6, 0.1, 0.05, 0.22, 0.03])
    if str(ht[0]) != 'none':
        tc = np.random.choice(colr, size=1, p=[0.2, 0.2, 0.15, 0.03, 0.1, 0.15, 0.17])
        hat_image = Image.open("img/"+str(ht[0]+tc[0])+".png")
    else:
        hat_image = Image.open("img/nohat.png")

    # Setup the Shirt
    sh = np.random.choice(shrt, size=1, p=[0.5, 0.25, 0.22, 0.03])
    bc = np.random.choice(colr, size=1, p=[0.2, 0.2, 0.15, 0.03, 0.1, 0.15, 0.17])
    shirt_image = Image.open("img/"+str(sh[0]+bc[0])+".png")

    # Setup the Smoke
    sk = np.random.choice(smok, size=1, p=[0.7, 0.14, 0.14, 0.02])
    if str(sk[0]) != 'none':
        smoke_image = Image.open("img/"+str(sk[0])+".png")
    else:
        smoke_image = Image.open("img/nocig.png")

    workdude = [hat_image, shirt_image, smoke_image]
    return workdude

while generator:
    dude = (randomizer())
    i += 1

    if dude not in dudes:
        dudes.append(dude)
        new_image = Image.new('RGBA',(32, 32), (250,250,250,0))
        new_image.paste(head,(0,0))
        new_image.paste(dude[0],(0,0),dude[0])
        new_image.paste(dude[1],(0,0),dude[1])
        new_image.paste(dude[2],(0,0),dude[2])
        new_image.save("img/test/dude{}.png".format(i))

        if len(dudes) == anz:
            print("{} ungerschidlechi dudes generiert".format(anz))
            print("und es het nume {} Iteratione brucht :)".format(i))
            generator=False

