#!usr/bin/python

print 'Content-type: text/html\n'

import cgi

import cgitb
cgitb.enable()

inputs = cgi.FieldStorage()
names = inputs.keys()

s = "<html><head><title>Questions that will never be answered</title></head><body>"

f = open("responses.txt", "a")
for n in names:
    s+= inputs[n].name + ": " + inputs[n].value + "<br>"
f.close()

s+= "</body></html>"

print s 




