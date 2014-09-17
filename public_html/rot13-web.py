#!/usr/bin/python
print "Content-type: text/html\n"

import cgitb
cgitb.enable()

import cgi

inputs = cgi.FieldStorage()

names = inputs.keys()

s = "<html><head></head><body>"

def rot13Char( c ):
    charNum = ord(c)
    if c < "N":
        charNum += 13
    elif c <= "Z":
        charNum -= 13
    elif c < "n":
        charNum += 13
    else:
        charNum -= 13
    return chr( charNum )

def rot13ify( s ):
    i = 0
    ns = ""
    while i < len(s):
        if (s[i] >= "A" and s[i] <= "Z" or
            s[i] >= "a" and s[i] <= "z"):
            ns+= rot13Char( s[i] )
        else:
            ns+= s[i]
        i+=1
    return ns

for n in names:
    s += n
    s += "\n"
    s += "rot13: " + rot13ify(n)
    
s += "</body></html>"

print s 
