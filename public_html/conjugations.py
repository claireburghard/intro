#!/usr/bin/python

print "Content-type: text/html\n"

def Table (myfile):
    f = open(myfile, "r")
    f1 = f.read()
    f.close()
    f2 = f1.split("\n")
    headings = f2[0]
    headings1 = headings.split(",")
    s = "<html>"
    s += "<head><title>"+ f.name +"</title></head>"
    s += "<body>"
    s += "<table boarder='1'>"
    s += "<tr>"
    for n in headings1:
        s += "<td><h1>"+ n +"</h1></td>"
    s += "</tr>"
    content = f2[1:]
    for n in content:
        line = n.split(",")
        s += "<tr>"
        for n in line:
            s += "<td>"+ n +"</td>"
        s += "</tr>"
    s += "</body>"
    s += "</html>"
    return s

print Table("conjugations.csv")


   
