story = "NAME was a ADJECTIVE ANIMAL who lived in CITY when he was AGE years old and liked to VERB when it was WEATHER."
names = ["Brendon","Antonia","Felix","Berlioz","Evelyn"]
adjectives = ["peculiar","fascinating","fusia","terrifying","quaint"]
animals = ["starfish","sloth","porcupine","Bengal tiger","meerkat"]
cities = ["San Francisco","Orleans","Dublin","Brussels","Sydney"]
ages = ["fourty nine","twenty","two","seventeen","one hundred and four","seventy five"]
verbs = ["play football","go fishing","see a movie","play Candyland","go thrift shopping"]
weather = ["snowing","hailing","raining","acid raining","sleeting"]

import random

def RANDOM (x):
    i = random.randrange (len(x)-1)
    return x[i]

print RANDOM (animals)
print RANDOM (weather)

def madlibs (x):
    answer = x.split(" ")
    iName = answer.index("NAME")
    answer.remove ("NAME")
    answer[iName] = RANDOM (names)
    iAdjective = answer.index("ADJECTIVE")
    iAnimal = answer.index("ANIMAL")
    iCity = answer.index("CITY")
    iAge = answer.index("AGE")
    iVerb = answer.index("VERB")
    iWeather = answer.index("WEATHER")
    
