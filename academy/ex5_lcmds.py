#!/usr/bin/python3.7

import os, subprocess

# kill a certain process
def killer(proc):
    answer = input(f"Do you want to kill process: {proc} [y/N]")
    if answer == "y":
        os.kill(int(proc), 9) and print("KILLED")


def finder(keyword):
    check=subprocess.check_output(['lsof | grep LISTEN'], shell=True).split()[1].decode('ascii')
    if check:
        print(f"Process fount! Id:{check}")
        killer(check)

try:
    finder(input("Process you want to find [LISTEN]: "))
except:
    print("\nError! Couldn't compute your request")

