#!/usr/bin/python

import random

print "content-type:text/html\n"

s = "When you're VERB in a WEATHER in CITY and it's HOLIDAY make sure to bring your NOUN"

replace = ["VERB", "WEATHER", "CITY", "HOLIDAY", "NOUN"]
verbs = ["eating", "swimming", "bathing", "lost"]
weather = ["heat wave", "blizzard", "hurricane", "rain"]
cities = ["Phoenix", "Brooklyn", "Toledo", "Juarez"]
holidays = ["rosh hashannah", "flag day", "eid", "easter"]
nouns = ["toothbrush", "towel", "cat", "toilet"]

def randomElement(g):
    return g[ random.randrange(len(g))]

myfile = open("madlibs2.csv","r")
readmyfile = myfile.read().strip("\n")
words = readmyfile.split(" ")
myfile.close()


for n in  replace:
    while n in words:
        i = words.index(n)
        if n == "VERB":
            words[i] = randomElement(verbs)
        elif n == "WEATHER":
            words[i] = randomElement(weather)
        elif n == "CITY":
            words[i] = randomElement(cities)
        elif n == "HOLIDAY":
            words[i] = randomElement(holidays)
        elif n == "NOUN":
            words[i] = randomElement(nouns)


print " ".join(words)
