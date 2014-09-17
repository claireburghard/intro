#!/usr/bin/python

print "Content-type: text/html\n"

f = open("music.csv~" , "r")
f1 = f.read()
myfile = f1.split("\n")
f.close()


print "<html><head><title>Data</title></head><body><h1>1000 Songs to Listen to Before You Die</h1><table border='1'>"


def data():
    headings = myfile[0].split(",")
    headings = headings[:2] + headings[3:4]
    for n in headings:
        print "<th>" + n + "</th>"
    data = myfile[1:]
    for n in data:
        print "<tr>"
        line = n.split(",")
        line = line[:2] + line[3:4]
        for x in line:
            print "<td>" + x + "</td>"
        print "</tr>"
    print "</table>"
data()
print "</body></html>"
