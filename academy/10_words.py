#!/usr/bin/python3.7

import argparse

parser = argparse.ArgumentParser(description="Search for word")
parser.add_argument('snippet', help="key 2 search 4 ")

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()


# Boring way
# matches = []
#
# for word in words:
#     if snippet in word.lower():
#             matches.append(word)
#
# Better way:
# matches [word for word in words if snippet in word.lower()]

print([word.strip() for word in words if snippet in word.lower()])


