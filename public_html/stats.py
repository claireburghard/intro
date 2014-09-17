mylist = [3,2,-6,-8,9,20]
positiveList = [4, 3, 7, 6, 8]
print mylist

def average (L):
    i = 0
    added = 0.0
    while i < len(L):
        added += L[i]
        i += 1
    answer = added/len(L)
    return answer

print average (mylist)

def smallest (L):
    newlist = sorted(L)
    answer = newlist[0]
    return answer

print smallest (mylist)

def biggest (L):
    newlist = sorted(L,reverse=True)
    answer = newlist[0]
    return answer

print biggest (mylist)

def median (L):
    answer = 0.0
    length = len(L)
    newlist = sorted(L)
    half = length/2
    if length%2 == 1:
        answer += newlist[half + 1]
    else:
        answer += (newlist[half] + newlist[half + 1]) / 2
    return answer

print median (mylist)

def barGraph (L):
    i = 0
    while i < len(L):
        print str(i) + ": " + "="*L[i]
        i += 1

print positiveList
barGraph (positiveList)






    




