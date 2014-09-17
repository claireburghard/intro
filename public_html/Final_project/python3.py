#!/usr/bin/python

import cgi

import cgitb
cgitb.enable()

print "Content-type: text/html\n"

inputs = cgi.FieldStorage()

html = "<html><head><title>My poem</title></head>"

if "love1" in inputs.keys():
    f = open("love1.txt" , "r")
    s = f.read()
    f.close()
elif "love2" in inputs.keys():
    f = open("love2.txt" , "r")
    s = f.read()
    f.close()
elif "love3" in inputs.keys():
    f = open("love3.txt" , "r")
    s = f.read()
    f.close()
elif "love4" in inputs.keys():
    f = open("love4.txt" , "r")
    s = f.read()
    f.close()
elif "pain1" in inputs.keys():
    f = open("pain1.txt" , "r")
    s = f.read()
    f.close()
elif "pain2" in inputs.keys():
    f = open("pain2.txt" , "r")
    s = f.read()
    f.close()
elif "pain3" in inputs.keys():
    f = open("pain3.txt" , "r")
    s = f.read()
    f.close()
elif "pain4" in inputs.keys():
    f = open("pain4.txt" , "r")
    s = f.read()
    f.close()
elif "life1" in inputs.keys():
    f = open("life1.txt" , "r")
    s = f.read()
    f.close()
elif "life2" in inputs.keys():
    f = open("life2.txt" , "r")
    s = f.read()
    f.close()
elif "life3" in inputs.keys():
    f = open("life3.txt" , "r")
    s = f.read()
    f.close()
elif "life4" in inputs.keys():
    f = open("life4.txt" , "r")
    s = f.read()
    f.close()
elif "death1" in inputs.keys():
    f = open("death1.txt" , "r")
    s = f.read()
    f.close()
elif "death2" in inputs.keys():
    f = open("death2.txt" , "r")
    s = f.read()
    f.close()
elif "death3" in inputs.keys():
    f = open("death3.txt" , "r")
    s = f.read()
    f.close()
elif "death4" in inputs.keys():
    f = open("death4.txt" , "r")
    s = f.read()
    f.close()
elif "experiences1" in inputs.keys():
    f = open("experiences1.txt" , "r")
    s = f.read()
    f.close()
elif "experiences2" in inputs.keys():
    f = open("experiences2.txt" , "r")
    s = f.read()
    f.close()
elif "experiences3" in inputs.keys():
    f = open("experiences3.txt" , "r")
    s = f.read()
    f.close()
elif "experiences4" in inputs.keys():
    f = open("experiences4.txt" , "r")
    s = f.read()
    f.close()
elif "people1" in inputs.keys():
    f = open("people1.txt" , "r")
    s = f.read()
    f.close()
elif "people2" in inputs.keys():
    f = open("people2.txt" , "r")
    s = f.read()
    f.close()
elif "people3" in inputs.keys():
    f = open("people3.txt" , "r")
    s = f.read()
    f.close()
elif "people4" in inputs.keys():
    f = open("people4.txt" , "r")
    s = f.read()
    f.close()

Q1 = inputs["Q1"].value
Q2 = inputs["Q2"].value
Q3 = inputs["Q3"].value
Q4 = inputs["Q4"].value
Q5 = inputs["Q5"].value

def writing():
    t = s.split(" ")
    for n in t:
        if n == "Q1":
	    i = t.index(n)
            t[i] = Q1
        elif n == "Q2":
	    i = t.index(n)
            t[i] = Q2
        elif n == "Q3":
	    i = t.index(n)
            t[i] = Q3
        elif n == "Q4":
	    i = t.index(n)
            t[i] = Q4
        elif n == "Q5":
	    i = t.index(n)
            t[i] = Q5
    poem = " ".join(t)
    return poem

p = writing()

html += "<body BGCOLOR='#F5A9F2'><center><h2>Your poem!</h2>"
html += "<form action='python4.py' method='POST'>"
html += "<h4>What would you like to name your poem?</h4>"
html += "<input type='text' name='title'><br><br>"
html += p
html += "<textarea name='poem' cols='40 rows='60'>"
html += p
html += "</textarea><br>"
html += "<b>Would you like to save this poem to our website's collection of poems? This will allow other users to view your poetry. If so, click 'submit'. If not, click 'start over' to get rid of this poem and start over.</b><br>"
html += "<input type='submit' name='preview' value='submit'><br>"
html += "<a href='choose.html'>Start over</a>"
html += "<br><br><a href='home.html'>Home</a>"
html += "</center></body></html>"

print html



        
    

