#!/usr/bin/python3

import sys

# Main function to check args
def main(argv):
    if len(argv) < 3:
        print("Please call the script like:\n./todo.py <add|complete> <\"taskname\">")
        exit(2)
    
    if sys.argv[1] == "add":
        add_todo(argv[2])
    elif sys.argv[1] == "complete":
        check_todo(argv[2])
    else:
        print("Either choose add or complete")

# Function to add todos
def add_todo(todo):
    with open('db.txt', "a") as f:
        print("Todo added.")
        f.write(todo + "\t open\n")


# Function to check and complete todos
def check_todo(todo):
    content = ""
    found = False 
    with open('db.txt', "r") as f:
        entries = f.readlines()
        for line in entries:
            if todo in line:
                found = True
                content += line.replace('open', 'done')
            else:
                content += line

    if found:
        with open('db.txt', "w") as f:
            print("Todo updated.")
            f.write(content)
    else:
        print(todo + " not found")

if __name__ == "__main__":
   main(sys.argv)
