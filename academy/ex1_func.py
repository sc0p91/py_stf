#!/usr/bin/python3.7

def repeater(message, amount):
        print(message * amount)

message = input("What message to you want me so say? ")
amount = input("How many times should I say it? ").strip()

if message:
    if not amount:
        amount=1
    try:
        repeater(message, int(amount))
    except:
        print(f"Whoopsie! Error")
else:
    print("Check input")

