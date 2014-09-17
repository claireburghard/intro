def getStatHeaders (myfile):
    f = open(myfile,"r")
    s = f.readlines()
    headers = s[0].split(",")
    return headers

print getStatHeaders ("bernie.csv")

def getStats (myfile):
    f = open(myfile,"r")
    s = f.readlines()
    stats = s[1:]
    return stats

print getStats ("bernie.csv")

def getStat (myfile,category):
    headers = getStatHeaders (myfile)
    stats = getStats(myfile)
    i = headers.index(category)
    answer = []
    z = 0
    for n in stats:
        year = n.split(",")
        answer += year[i]
    return answer

print getStat ("bernie.csv","HR")

def sportsStats (file1, file2, category1, category2, category3):
    stats1.1 = getStat (file1, category1)
    stats1.2 = getStat (file1, category2)
    stats1.3 = getStat (file1, category3)
    stats2.1 = getStat (file1, category1)
    stats2.2 = getStat (file1, category2)
    stats2.3 = getStat (file1, category3)
    avg1.1 = 0
    avg1.2 = 0
    avg1.3 = 0
    avg2.1 = 0
    avg2.2 = 0
    avg2.3 = 0
    for n in stats 1.1:
        avg1.1 += int(n)
    avg1.1 = avg1.1/len(avg1.1)
    for n in stats 1.2:
        avg1.2 += int(n)
    avg1.2 = avg1.2/len(avg1.2)
    for n in stats 1.3:
        avg1.3 += int(n)
    avg1.3 = avg1.3/len(avg1.3)
    for n in stats 2.1:
        avg2.1 += int(n)
    avg2.1 = avg2.1/len(avg2.1)
    for n in stats 2.2:
        avg2.2 += int(n)
    avg2.2 = avg2.2/len(avg2.2)
    for n in stats 2.3:
        avg2.3 += int(n)
    avg2.3 = avg2.3/len(avg2.3)
    print "Bernie Williams Stats:" + "\n" + category1 + ":" + 
    
