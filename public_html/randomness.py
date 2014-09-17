import random

def randomList (size, n):
    answer = []
    while len(answer) < size:
        answer.append(random.randrange(n))
    return answer

print randomList (7,80)

def randomIP ():
    answer = str(random.randrange(225))
    i = 0
    while i < 3:
        answer += "." + str(random.randrange(225))
        i += 1
    return answer

print randomIP ()


