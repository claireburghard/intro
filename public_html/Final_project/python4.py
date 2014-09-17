#!/usr/bin/python

import cgi

import cgitb
cgitb.enable()

print "Content-type: text/html\n"

inputs = cgi.FieldStorage()

if "preview" in inputs.keys():
    title = inputs['title'].value
    poem = inputs['poem'].value
    html = "<html><head><title>Preview</title></head><body BGCOLOR='#F5A9F2'><center><h1>"
    html += title
    html += "</h1>"
    html += poem
    html += "<i>Thank you for writing this wonderful poem! You can click <a href='poems.html'>here</a> to view your poem, along with other submissions.</i>"
    html += "</center></body></html>"
    mypoem = "<b>" + title + "</b>"+ "<br><br> " + poem + "<br> <hr>" 
    f = open("poems.html" , "a")
    f.write(mypoem)

print html


