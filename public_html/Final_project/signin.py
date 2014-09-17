#!/usr/bin/python

import cgi

import cgitb
cgitb.enable()

print "Content-type: text/html\n"

inputs = cgi.FieldStorage()

print "<html><body BGCOLOR='#F5A9F2'><head><title>Results</title></head>"

def registering():
    registered = open("registered.txt" , "r")
    rstring = registered.read()
    registered.close()
    if "register" in inputs.keys():
        rname = inputs["signname"].value
        rpname = inputs["signpw"].value
        s=" "
        if rname in rstring:
            s+= "You already have an account with us, or someone already has that name. Please try again, or login.<br><br><a href='home.html'>Home</a>"
        else:
            r = open("registered.txt" , "a")
            r.write(rname + ":" + rpname + "\n")
            s+= "Thank you for signing up with us! Please go to the previous page and sign in to start writing your poems.<br><br><a href='home.html'>Home</a>"
            r.close()
        print s

registering()

def signin():
    registered = open("registered.txt" , "r")
    rstring = registered.read()
    registered.close()
    if "login" in inputs.keys():
        name = inputs["loginname"].value
        password = inputs["loginpw"].value
        x = name + ":" + password + "\n"
        if x in rstring:
            print "<center><h1>Welcome Back! Please click <a href='choose.html'>here</a> to begin your poem.</h1></center><br><a href='home.html'>Home</a>"
        else:
            print "<center><h3>We're sorry, but you are not registered with us yet, or maybe you just typed in your username and password incorrectly. Please return to the previous page and try again.</h3></center><br><a href='home.html'>Home</a>"

signin()

print "</body></html>"	




