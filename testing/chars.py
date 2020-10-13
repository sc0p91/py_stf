#!/usr/bin/python3.8

import sys, os


def main(argv):
    inp = ""

    if len(sys.argv) == 1:
        inputter()
    else:
        for content in sys.argv:
            if content != sys.argv[0]:
                inp += content + " " 
        convertor(inp)

def inputter():
    inp = input("String to convert: ")
    convertor(inp)

def convertor(inp):
    sum = 0
    csum = 0
    splitted = [char for char in inp]
    for c in splitted:
        print ("Value \"" + c + "\": " + str(ord(c)))
        sum = sum + ord(c)
    print("Summe: " + str(sum))

    fp = digitsum(sum)
    while fp > 9:
        fp = digitsum(fp)

def digitsum(sum):
    ds = 0

    while sum:
        ds += sum % 10
        sum = sum // 10
    print("QS: " + str(ds))
    return ds


if __name__ == "__main__":
    main(sys.argv[1:])
