#!/usr/bin/python

import cgi

import cgitb
cgitb.enable()

print "Content-type: text/html\n"

inputs = cgi.FieldStorage()

print "<html><head><title>Step 1</title></head><body>"

def topic():
    if "love" in inputs.keys():
        print
        "<center>_____</center></body></html>"
