#!/usr/bin/python

import cgi

import cgitb
cgitb.enable()

print "Content-type: text/html\n"

inputs = cgi.FieldStorage()

print "<html><body BGCOLOR='#F5A9F2'><head><title>Results</title></head>"

def choose():
    if "love" in inputs.keys():
        print "<center>"
        print "<h1>What do you think of love? (Please choose one quote that resonates with you the most.)</h1>"
        print "<h3>"
        print "<a href='love1.html'>The heart is the only broken instrument that works.-T.E. Kalem</a> <br><br>"
        print "<a href='love2.html'>Where there is love there is life.-Mahatma Gandhi </a> <br><br>"
        print "<a href='love3.html'>You don't love someone because they're perfect, you love them in spite of the fact that they're not. - Jodi Picoult</a> <br><br>"
        print "<a href='love4.html'>Love can sometimes be magic. But magic can sometimes just be an illusion.-Javan</a> <br><br>"
        print "</h3>"
        print "</center>"
    elif "pain" in inputs.keys():
        print "<center>"
        print "<h1>What do you think of pain? (Please choose one quote that resonates with you the most.)</h1>"
        print "<h3>"
        print "<a href='pain1.html'>The marks humans leave are too often scars.-John Green</a> <br><br>"
        print "<a href='pain2.html'>Numbing the pain for a while will make it worse when you finally feel it.-J.K. Rowling </a> <br><br>"
        print "<a href='pain3.html'>One word/ Frees us of all the weight and pain of life:That word is love.-Sophocles</a> <br><br>"
        print "<a href='pain4.html'>Behind every beautiful thing, there's some kind of pain.-Bob Dylan</a> <br><br>"
        print "</h3>"
        print "</center>"
    elif "life" in inputs.keys():
        print "<center>"
        print "<h1>What is the meaning of life? (Please choose one quote that resonates with you the most.)</h1>"
        print "<h3>"
        print "<a href='life1.html'>You will never live if you are looking for the meaning of life.-Albert Camus</a> <br><br>"
        print "<a href='life2.html'>The best things in life make you sweaty.-Edgar Allan Poe </a> <br><br>"
        print "<a href='life3.html'>The Ultimate Answer to Life, The Universe and Everything is...42!-Douglas Adams</a> <br><br>"
        print "<a href='life4.html'>''But for what purpose was the earth formed?' asked Candide. 'To drive us mad,' replied Martin.'-Voltaire</a> <br><br>"
        print "</h3>"
        print "</center>"
    elif "death" in inputs.keys():
        print "<center>"
        print "<h1>What do you think about death? (Please choose one quote that resonates with you the most.)</h1>"
        print "<h3>"
        print "<a href='death1.html'>I'm not afraid of death; I just don't want to be there when it happens.-Woody Allen</a> <br><br>"
        print "<a href='death2.html'>To the well-organized mind, death is but the next great adventure.-J.K. Rowling</a> <br><br>"
        print "<a href='death3.html'>I'm the one that's got to die when it's time for me to die, so let me live my life the way I want to.-Jimi Hendrix</a> <br><br>"
        print "<a href='death4.html'>Unbeing dead isn't being alive.-E.E. Cummings</a> <br><br>"
        print "</h3>"
        print "</center>"    
    elif "experiences" in inputs.keys():
        print "<center>"
        print "<h1>How has a recent experience effected you? (Please choose one quote that resonates with you the most.)</h1>"
        print "<h3>"
        print "<a href='experiences1.html'>Don't cry because it's over, smile because it happened.-Dr.Seuss</a> <br><br>"
        print "<a href='experiences2.html'>All I have seen teaches me to trust the Creator for all I have not seen.-Ralph Waldo Emerson </a> <br><br>"
        print "<a href='experiences3.html'>All knowledge hurts.-Cassandra Clare</a> <br><br>"
        print "<a href='experiences4.html'>I think the highest and lowest points are the important ones. Anything else is just...in between.-Jim Morrison</a> <br><br>"
        print "</h3>"
        print "</center>"
    elif "people" in inputs.keys():
        print "<center>"
        print "<h1>What do you think of a particular person? (Think of one person, and please choose one quote that resonates with you the most.)</h1>"
        print "<h3>"
        print "<a href='people1.html'>It is not a lack of love, but a lack of friendship that makes unhappy marriages.-Friedrich Nietzsche</a> <br><br>"
        print "<a href='people2.html'>If you live to be a hundred, I want to live to be a hundred minus one day so I never have to live without you.-A.A. Milne </a> <br><br>"
        print "<a href='people3.html'>The truth is, everyone is going to hurt you. You just got to find the ones worth suffering for.-Bob Marley</a> <br><br>"
        print "<a href='people4.html'>It is easier to forgive an enemy than to forgive a friend.-William Blake</a> <br><br>"
        print "</h3>"
        print "</center>" 
    print "<br><br><a href='home.html'>Home</a></body></html>"	

choose()
