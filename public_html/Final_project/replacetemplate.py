#!/usr/bin/python

import cgi

import cgitb
cgitb.enable()

print "Content-type: text/html\n"

inputs = cgi.FieldStorage()
f=open("poemexample.txt"
r=f.read()
f.close()
s = r

replace = ["a1", "a2", "a3", "a4", "a5", "etcetc"]
a1=["___"]
a2=["____"]
etc etc


for n in  replace:
    while n in s:
        if n == "a1":
            words[i] = randomElement(verbs)
        elif n == "a2":
            words[i] = randomElement(weather)
        elif n == "a3":
            words[i] = randomElement(cities)
        elif n == "a4":
            words[i] = randomElement(holidays)
        elif n == "etc":
            words[i] = randomElement(nouns)


print " ".join(__)
