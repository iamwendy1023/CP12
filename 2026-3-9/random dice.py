#Create a list of random numbers chosen from 1 to 6 (random dice)
#Then count how many 1s, 2s, ... 6s are in the list.
#Is Python random function uniform?
import random
r = []
for i in range(100):
    r.append(random.randint(1,6))
for x in range(1,7):
    c = 0
    for y in r:
        if y == x:
            c = c + 1
    print(x, c)