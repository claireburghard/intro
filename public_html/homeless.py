#!/usr/bin/python

f = open("homelesspeople.csv" , "r")
myfile = f.read().split("\r")
f.close()

print "<html><body><table boarder='1'>"

def data():
    headings = myfile[0].split(",")
    for n in headings:
        print "<th>" + n + "</th>"
    data = myfile[1:]
    for n in myfile:
        print "<tr>"
        line = n.split(",")
        for x in line:
            print "<td>" + x + "</td>"
        print "</td>"
    print "</table>"

print "</body></html>"

data ()


