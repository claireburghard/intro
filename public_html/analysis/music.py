#!/usr/bin/python
# -*- coding: utf-8 -*-

print "Content-type: text/html\n"

f = open("music.csv~" , "r")
f1=f.read()
f2=f1.strip()
myfile = f1.split("\n")
f.close()

print "<html><head><title>Song Trends of the 20th and 21st Centuries</title></head><body>"
print "<h3>Claire Burghard and Remi Moon, Period 8</h3>"
print "<h1><center>Song Trends of the 20th and 21st Centuries</center></h1>"

print "<h1>Why?</h1>Over the last few decades, music has been increasingly important in peoples' lives. Although a wide range of types of music have come from the 20 and 21st centuries, we observe a pattern in the topics of music. There are certain timeless subjects that we see songwriters use over and over again. Let's look at a list of 1000 of the most popular songs of the 20th and 21st centuries: '1000 Songs to Listen to Before You Die,' compiled by the popular British music blog guardian.co.uk ("+"<a href='http://www.guardian.co.uk/news/datablog/2009/mar/20/1'>see the blog here!</a>"+"). This list was made based on a survey of frequent blog viewers, making it an acurate representation of modern popular music."

print "<h1>The Data</h1><a href='musicdata.py'>View the chart here!</a>"

print "That's a lot of information! Let's narrow it down a bit."

print "<h1>The Analysis</h1>"

print "<h3>Popularity of Each Song Subject</h3>"

print "<table border='1'>"

def analysis ():
    print "<table border='1'>"
    data = myfile[1:]
    love = 0
    heartbreak = 0
    peopleandplaces = 0
    sex = 0
    politicsandprotest = 0
    lifeanddeath = 0
    partysongs = 0
    for z in data:
        w = z.split(",")
        for n in w:
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
    d = [love,heartbreak,peopleandplaces,sex,politicsandprotest,lifeanddeath,partysongs]
    keys = ["Love","Heartbreak","People and Places","Sex","Politics and protest","Life and death","Party songs"]
    print "<tr>"
    for n in keys:
        print "<th>" + n + "</th>"
    print "</tr><tr>"
    for x in d:
        print "<td>" + str(x) + "</td>"
    print "</tr>"
    print "</table>"

analysis()

print "This table shows us the number of songs out of the 1000 'Songs to Listen to Before You Die' that fall under each subject. We can observe that according to this data set, Party Songs is the most popular topic, with 162 hits. <b>RAISE THE ROOF!</b>"
print "Now lets look at each decade."
print "<h3>Subjects of Songs by Decade</h3>"

data = myfile[1:]
q = []
for n in data:
    line = n.split(",")
    if len(line) > 3:
        year = line[3]
    if str(year) in q:
        q=q
    else:
        q.append(year)
q=sorted(q)[1:]
tens=[]
twenties=[]
thirties=[]
fourties=[]
fifties=[]
sixties=[]
seventies=[]
eighties=[]
nineties=[]
twothousands=[]
for x in q:
    if int(x)<1920:
        tens.append(x)
    elif int(x)<1930 and int(x)>=1920:
        twenties.append(x)
    elif int(x)<1940 and int(x)>=1930:
        thirties.append(x)
    elif int(x)<1950 and int(x)>=1940:
        fourties.append(x)
    elif int(x)< 1960 and int(x)>=1950:
        fifties.append(x)
    elif int(x) <1970 and int(x)>=1960:
        sixties.append(x)
    elif int(x)<1980 and int (x)>=1970:
        seventies.append(x)
    elif int(x)<1990 and int(x)>=1980:
        eighties.append(x)
    elif int(x)<2000 and int(x)>=1990:
        nineties.append(x)
    else:
        twothousands.append(x)



love=myfile[1:140]
ten=0
twentie=0
thirtie=0
fourtie=0
fiftie=0
sixtie=0
seventie=0
eightie=0
ninetie=0
twothousand=0
for x in love:
    data=x.split(',')
    if data[3] in tens:
        ten+=1
    elif data[3] in twenties:
        twentie+=1
    elif data[3] in thirties:
        thirtie+=1
    elif data[3] in fourties:
        fourtie+=1
    elif data[3] in fifties:
        fiftie+=1
    elif data[3] in sixties:
        sixtie+=1
    elif data[3] in seventies:
        seventie+=1
    elif data[3] in eighties:
        eightie+=1
    elif data[3] in nineties:
        ninetie+=1
    elif data[3] in twothousands:
        twothousand+=1

heartbreak=myfile[141:286]
tenh=0
twentieh=0
thirtieh=0
fourtieh=0
fiftieh=0
sixtieh=0
seventieh=0
eightieh=0
ninetieh=0
twothousandh=0
for x in heartbreak:
    data=x.split(',')
    if data[3] in tens:
        tenh+=1
    elif data[3] in twenties:
        twentieh+=1
    elif data[3] in thirties:
        thirtieh+=1
    elif data[3] in fourties:
        fourtieh+=1
    elif data[3] in fifties:
        fiftieh+=1
    elif data[3] in sixties:
        sixtieh+=1
    elif data[3] in seventies:
        seventieh+=1
    elif data[3] in eighties:
        eightieh+=1
    elif data[3] in nineties:
        ninetieh+=1
    elif data[3] in twothousands:
        twothousandh+=1

people=myfile[286:430]
tenpp=0
twentiepp=0
thirtiepp=0
fourtiepp=0
fiftiepp=0
sixtiepp=0
seventiepp=0
eightiepp=0
ninetiepp=0
twothousandpp=0
for x in people:
    data=x.split(',')
    if data[3] in tens:
        tenpp+=1
    elif data[3] in twenties:
        twentiepp+=1
    elif data[3] in thirties:
        thirtiepp+=1
    elif data[3] in fourties:
        fourtiepp+=1
    elif data[3] in fifties:
        fiftiepp+=1
    elif data[3] in sixties:
        sixtiepp+=1
    elif data[3] in seventies:
        seventiepp+=1
    elif data[3] in eighties:
        eightiepp+=1
    elif data[3] in nineties:
        ninetiepp+=1
    elif data[3] in twothousands:
        twothousandpp+=1

sex=myfile[431:561]
sten=0
stwentie=0
sthirtie=0
sfourtie=0
sfiftie=0
ssixtie=0
sseventie=0
seightie=0
sninetie=0
stwothousand=0
for x in sex:
    data=x.split(',')
    if data[3] in tens:
        sten+=1
    elif data[3] in twenties:
        stwentie+=1
    elif data[3] in thirties:
        sthirtie+=1
    elif data[3] in fourties:
        sfourtie+=1
    elif data[3] in fifties:
        sfiftie+=1
    elif data[3] in sixties:
        ssixtie+=1
    elif data[3] in seventies:
        sseventie+=1
    elif data[3] in eighties:
        seightie+=1
    elif data[3] in nineties:
        sninetie+=1
    elif data[3] in twothousands:
        stwothousand+=1

politics=myfile[562:702]
pten=0
ptwentie=0
pthirtie=0
pfourtie=0
pfiftie=0
psixtie=0
pseventie=0
peightie=0
pninetie=0
ptwothousand=0
for x in politics:
    data=x.split(',')
    if data[3] in tens:
        pten+=1
    elif data[3] in twenties:
        ptwentie+=1
    elif data[3] in thirties:
        pthirtie+=1
    elif data[3] in fourties:
        pfourtie+=1
    elif data[3] in fifties:
        pfiftie+=1
    elif data[3] in sixties:
        psixtie+=1
    elif data[3] in seventies:
        pseventie+=1
    elif data[3] in eighties:
        peightie+=1
    elif data[3] in nineties:
        pninetie+=1
    elif data[3] in twothousands:
        ptwothousand+=1

life=myfile[703:833]
lten=0
ltwentie=0
lthirtie=0
lfourtie=0
lfiftie=0
lsixtie=0
lseventie=0
leightie=0
lninetie=0
ltwothousand=0
for x in life:
    data=x.split(',')
    if data[3] in tens:
        lten+=1
    elif data[3] in twenties:
        ltwentie+=1
    elif data[3] in thirties:
        lthirtie+=1
    elif data[3] in fourties:
        lfourtie+=1
    elif data[3] in fifties:
        lfiftie+=1
    elif data[3] in sixties:
        lsixtie+=1
    elif data[3] in seventies:
        lseventie+=1
    elif data[3] in eighties:
        leightie+=1
    elif data[3] in nineties:
        lninetie+=1
    elif data[3] in twothousands:
        ltwothousand+=1

party=myfile[834:995]
psten=0
pstwentie=0
psthirtie=0
psfourtie=0
psfiftie=0
pssixtie=0
psseventie=0
pseightie=0
psninetie=0
pstwothousand=0
for x in party:
    data=x.split(',')
    if data[3] in tens:
        psten+=1
    elif data[3] in twenties:
        pstwentie+=1
    elif data[3] in thirties:
        psthirtie+=1
    elif data[3] in fourties:
        psfourtie+=1
    elif data[3] in fifties:
        psfiftie+=1
    elif data[3] in sixties:
        pssixtie+=1
    elif data[3] in seventies:
        psseventie+=1
    elif data[3] in eighties:
        pseightie+=1
    elif data[3] in nineties:
        psninetie+=1
    elif data[3] in twothousands:
        pstwothousand+=1
        
print "<table border='1'>"
keys = ["Decade","Love","Heartbreak","People and Places","Sex","Politics and protest","Life and death","Party songs"]
print "<tr>"
for n in keys:
    print "<th>" + n + "</th>"
    
print "</tr><tr>"
TENS=[ten,tenh,tenpp,sten,pten,lten,psten]
print "<td>10's</td>"
for n in TENS:
    print "<td>"+ str(n)+"</td>"
    
print "</tr><tr>"
TWENTIE=[twentie,twentieh,twentiepp,stwentie,ptwentie,ltwentie,pstwentie]
print "<td>20's</td>"
for n in TWENTIE:
    print "<td>"+ str(n)+"</td>"
print "</tr><tr>"

THIRTIES=[thirtie,thirtieh,thirtiepp,sthirtie,pthirtie,lthirtie,psthirtie]
print "<td>30's</td>"
for n in THIRTIES:
    print "<td>"+ str(n)+"</td>"
print "</tr><tr>"

FOURTIES=[fourtie,fourtieh,fourtiepp,sfourtie,pfourtie,lfourtie,psfourtie]
print "<td>40's</td>"
for n in FOURTIES:
    print "<td>"+ str(n)+"</td>"
print "</tr><tr>"

FIFTIES=[fiftie,fiftieh,fiftiepp,sfiftie,pfiftie,lfiftie,psfiftie]
print "<td>50's</td>"
for n in FIFTIES:
    print "<td>"+ str(n)+"</td>"
print "</tr><tr>"

SIXTIES=[sixtie,sixtieh,sixtiepp,ssixtie,psixtie,lsixtie,pssixtie]
print "<td>60's</td>"
for n in SIXTIES:
    print "<td>"+ str(n)+"</td>"
print "</tr><tr>"

SEVENTIES=[seventie,seventieh,seventiepp,sseventie,pseventie,lseventie,psseventie]
print "<td>70's</td>"
for n in SEVENTIES:
    print "<td>"+ str(n)+"</td>"

print "</tr><tr>"
EIGHTIES=[eightie,eightieh,eightiepp,seightie,peightie,leightie,pseightie]
print "<td>80's</td>"
for n in SEVENTIES:
    print "<td>"+ str(n)+"</td>"

print "</tr><tr>"
NINETIES=[ninetie,ninetieh,ninetiepp,sninetie,pninetie,lninetie,psninetie]
print "<td>90's</td>"
for n in NINETIES:
    print "<td>"+ str(n)+"</td>"
    
print "</tr><tr>"
TWOTHOUSANDS=[twothousand,twothousandh,twothousandpp,stwothousand,ptwothousand,ltwothousand,pstwothousand]
print "<td>2000's</td>"
for n in TWOTHOUSANDS:
    print "<td>"+ str(n)+"</td>"
print "</tr></table>"

print "We can observe a few things from this chart. First, it's clear that the more recent the decade, the more imformation the data set gives us. The survey favors more recent songs, which is why there are few falling under the early decades of the 20th century, and many more falling under the 60s through the 2000s. Looking more closely at each decade, there are some very interesting trends. Beginning with the 1920s, 30s, 40s, and 50s, People and Places are the most popular subjects.But once we venture into the 60s, a revolutionary time for music, the subjects of Love, Politics and Protest, and Sex begin to dominate. By the 70s, 80s, and 90s, Party Songs and Sex are the most popular topics. Historically, this is not suprising. The 60s were a time of political unrest and the sexual revolution, specifically in the western world. The cultural change of the 60s set the stage for the rest of the 20th century, reflected in the shift to more provacative topics than People and Places, like Sex and Party Songs. It is interesting to see how music reflects its time."

print "<h1>The Conclusion</h1>"
print "Our data successfully reflected the cultural history of the 20th and 21st centuries, in an interesting way. However, to really make a point and to dig deeper into this history, one might want to use more solid data. A survey of 21st century people might be biast. Maybe facts on the top songs of each year would be more accurate. Still, the data gives an interesting perspective on the music of the last century."

print "<h1>Sources</h1>"
print "<a href='https://github.com/seancarmody/stubborn-mule/blob/master/Guardian-Music/1000.csv'>The csv file</a>"+"\n"+"<a href='http://www.guardian.co.uk/news/datablog/2009/mar/20/1'>The Blog</a>"
print "</body></html>"

