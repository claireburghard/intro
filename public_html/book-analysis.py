f = open("book.txt" , "r")
b = f.read()
f.close()

words = b.split()
for n in words:
    n = n.strip('''.,?![]()'";:''').lower()

def analysis():
    d = {}
    for n in words:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    print d
    
analysis

        
    
