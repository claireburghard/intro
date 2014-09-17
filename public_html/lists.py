def findList (L,x):
    if x in L:
        y = L.index(x)
    else:
        y = -1
    return y

kitties = ['meow','purr','whiskers']
print findList (kitties, 'purr')
print findList (kitties, 4)

def sumList (L):
    i = 0
    answer = 0
    while i < len(L):
        answer += L[i]
        i += 1
    return answer

print sumList ([1,2,3,4,5])

def doublify (L):
    d = 0
    while d < len(L):
        value = L.pop(0) * 2
        L.append (value)
        d += 1
    return L

print doublify ([1,2,3,4])
