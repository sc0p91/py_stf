#!/usr/bin/python3.7

from time import localtime, mktime, strftime

start_time = localtime()
print(f"Time startet: {strftime('%X', start_time)}")

# Wait for user input
input("Press 'Enter' to stop timer")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Time startet: {strftime('%X', stop_time)}")
print(f"Total time: {int(difference)} seconds")
