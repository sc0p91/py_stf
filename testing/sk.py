#!/usr/bin/python3
    
import string, time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def key_sender(input):
    time.sleep(3)
    for x in range (0, 10):
        output = (f"{str(time.time())}: {input}")
        keyboard.type(output)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

input = input("Enter Message: ")

if len(input) > 0:
    key_sender(input)
else:
    print("Error")
