def sumDigits (k):
    q = 0
    while k > 0:
        print "q:" + str(q)
        print "k:" + str(k) + "\n"
        q = q + k % 10
        k = k / 10
    return q
    print q

def squares (k):
    while k >= 0:
        print str(k) + "**2 = " + str(k**2) + "\n"
        k = k - 1
        
def prodSum (a,b):
    product = a*b
    productsentence = "the <i>product</i> of " + str(a) + " and " + str(b) + " is <b>" + str(product) + "</b>"
    SUM = a+b
    sumsentence = "the <i>sum</i> of " + str(a) + " and " + str(b) + " is <b>" + str(SUM) + "</b>"
    print productsentence
    print sumsentence
    
