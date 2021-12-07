import os

os.chdir('advent_2021/3')

def ltod(l):
    sum = 0
    e = 1
    while(len(l) > 0):
        n = l.pop()
        sum += n * e
        e *= 2
    return sum

def bitcount(lol, pos):
    sum = 0
    for n in lol:
        sum += n[pos]
    return(len(lol) - sum, sum)

oxygen_list = []
with open("input.txt", "r") as f:
    for line in f:
        n = []
        for c in line.rstrip():
            n.append(int(c))
        oxygen_list.append(n)

carbo_list = oxygen_list.copy()

pos = 0
while(len(oxygen_list) > 1):
    (n_0, n_1) = bitcount(oxygen_list, pos)
    if n_1 >= n_0:
        oxygen_list = list(filter(lambda n: n[pos] == 1, oxygen_list))
    else:
        oxygen_list = list(filter(lambda n: n[pos] == 0, oxygen_list))   
    pos += 1


pos = 0
while(len(carbo_list) > 1):
    (n_0, n_1) = bitcount(carbo_list, pos)
    if n_1 >= n_0:
        carbo_list = list(filter(lambda n: n[pos] == 0, carbo_list))
    else:
        carbo_list = list(filter(lambda n: n[pos] == 1, carbo_list))  
    pos += 1


oxygen = ltod(oxygen_list[0])
carbo = ltod(carbo_list[0])

# 2039 3649 7440311
print(oxygen, carbo, oxygen * carbo)