def problem1 (q):
    k=0
    answer=0
    while k < q:
        print "k =" + str(k)
        if (k % 3 == 0) or (k % 5 == 0):
            answer = answer + k
            k = k + 1
            print "answer =" + str(answer)
        else: k = k + 1
