#!/usr/bin/python3

names = []
nouns = []
verbs = []
adjes = []

print("Input 2 names:")
for i in range(0,2):
    name = str(input())
    names.append(name)

print("Input 3 nouns:")
for i in range(0,3):
    noun = str(input())
    nouns.append(noun)

print("Input 3 verbs:")
for i in range(0,3):
    verb = str(input())
    verbs.append(verb)

print("Input 5 adjectives:")
for i in range(0,5):
    adj = str(input())
    adjes.append(adj)


print(names, nouns, verbs, adjes)

print(f"Dr {adjes[4]} {names[0]} und {adjes[3]} {names[1]}")
print(f"{verbs[0]} mit ihrem {adjes[2]} {nouns[0]}.")
print(f"När {verbs[1]} plötzlech ihre {nouns[1]} und")
print(f"sofort {verbs[2]} {names[0]}'s {adjes[1]} {nouns[2]}") 
print(f"Isch das nid {adjes[0]}?")
