#!/usr/bin/python3.7

import argparse
import sys

# Build the parser
parser = argparse.ArgumentParser(description='Read a file and output it in reverse')
parser.add_argument('filename', help='Input file to read')
parser.add_argument('--limit', '-l', type=int, help='Numer of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s v.1.0')

# Parse the arguments
args = parser.parse_args()

# Test if the file exists
try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(err)
    sys.exit(2)
else:
# read the file, reverse the contents and print them out
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
