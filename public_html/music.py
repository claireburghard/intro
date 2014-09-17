#!/usr/bin/python

print "Content-type: text/html\n"

f = open("music.csv" , "r")
f1 = f.read()
myfile = f1.split("\n")
f.close()

print "<html><body><table border='1'>"

def data():
    headings = myfile[0].split(",")
    headings = headings[:-1]
    for n in headings:
        print "<th>" + n + "</th>"
    data = myfile[1:]
    for n in data:
        print "<tr>"
        line = n.split(",")
        line = line[:-1]
        for x in line:
            print "<td>" + x + "</td>"
        print "</tr>"
    print "</table>"

data ()

def analysis ():
    print "<table border='1'"
    print "</table>
    love = 0
    heartbreak = 0
    peopleandplaces = 0
    sex = 0
    politicsandprotest = 0
    lifeanddeath = 0
    partysongs = 0
    d = {}
    for n in data:
        if n == "Love":
            love += 1
         if n == "Heartbreak":
            heartbreak += 1
        if n == "People and places":
            peopleandplaces += 1
        if n == "Sex":
            sex += 1
        if n == "Politics and protest":
            politicsandprotest += 1
        if n == "Life and death":
            lifeanddeath += 1
        if n == "Party songs":
            partysongs += 1
    
            
    
    

print "</body></html>"
