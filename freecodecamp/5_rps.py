#!/usr/bin/python3
import random

print("Let's Play RPS! ['r', 'p' or 's'] ")
weapon = ['Rock','Paper','Scissors']
chosen = input("Player: ")

random.seed()
rand = random.randint(0,2)

if chosen == "r":
    chosen = 0
if chosen == "p":
    chosen = 1
if chosen == "s":
    chosen = 2

print(f"Computer: {weapon[rand]}")

if rand == chosen:
    win = 3
elif rand == 0:
    if chosen == 1:
        win = 1
    else:
        win = 0
elif rand == 1:
    if chosen == 0:
        win = 0
    else:
        win = 1
elif rand == 2:
    if chosen == 0:
        win = 1
    else:
        win = 0
if win == 1:
    print("Player wins!")
elif win == 0:
    print("Player loses!")
else:
    print("It's a draw!")

