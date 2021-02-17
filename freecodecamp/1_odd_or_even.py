#!/usr/bin/python3

def checker(numb):
    if numb % 2 == 0:
        print("even!")
    else:
        print("odd!")

while True:
    try:
        numb = int(input("What number are you thinking? "))
        checker(numb)
    except ValueError:
        print("Not a valid number...")

