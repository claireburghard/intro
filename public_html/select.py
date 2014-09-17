import os
import random

def dirInfo ():
    x = os.getcwd()
    print "current working directory:" + x
    levels = x.split("/")
    answer = 0
    for n in levels:
        answer += 1
    print "depth = " + str(answer)

dirInfo()
    
def select1 (myfile):
    f = open(myfile, "r")
    fstring = f.read()
    flist = fstring.split(",")
    randomNum = random.randrange(len(flist))
    answer = flist[randomNum]
    return answer

print select1 ("select1.csv")

def select2 (myfile, integer):
    f = open(myfile, "r")
    fstring = f.read()
    flist = fstring.split ("\n")
    period1 = flist[0]
    period2 = flist[1]
    period3 = flist[2]
    periodOne = period1.split(",")
    periodTwo = period2.split(",")
    periodThree = period3.split(",")
    
    
                           
    
