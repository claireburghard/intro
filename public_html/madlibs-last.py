#!/usr/bin/python

import random

print "content-type:text/html\n"

s = open("frost.csv", "r")
poem = s.read()
splitpoem = poem.split(" ")

keywords = open("keywords.csv", "r")
keywords1 = keywords.readlines()
keywords.close()
d = {}
l = []
for n in keywords1:
    z = n.strip("\n")
    l = z.split(",")
    d[l[0]] = l[1:]

keys = d.keys()

def randomElement(g):
    return g[ random.randrange(len(g))]

for n in splitpoem:
    i = splitpoem.index(n)
    for k in keys:
        if n == k:
            splitpoem[i] = randomElement(d[k])

print " ".join(splitpoem)

