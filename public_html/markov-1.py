def readbook(mybook):
    f = open(mybook, "r")
    book = f.read()
    f.close()
    words = book.split()
    wordlist = []
    for n in words:
        wordlist.append(n.lower().strip(''':;'"()[]-_.?!'''))
    return words

readbook("book.txt")

def makeChains (s):
    pairs = []
    i1 = 0
    i2 = 1
    while i2 < len(s):
        pairs.append(s[i1] + " " + s[i2])
        i1 += 1
        i2 += 1
    for key in pairs:
        for values in s:
            
    d = {}
    

     



        
