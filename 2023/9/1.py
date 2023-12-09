import sys
import re


sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2023', '9')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def solve(a):
    lol = []
    lol.append(a)
    done = False
    while not done:
        nl = []
        for j in range(1,len(lol[-1])):
            nl.append(lol[-1][j] - lol[-1][j-1])

        tl = list(filter(lambda e: e!=0, nl))
        if len(tl)==0:
            done = True
        else:
            lol.append(nl)
    for i in range(len(lol)-1, 0, -1):
        lol[i-1].append(lol[i-1][-1]+lol[i][-1])
    return(lol[0][-1])    


def solve2(a):
    lol = []
    lol.append(a)
    done = False
    while not done:
        nl = []
        for j in range(1,len(lol[-1])):
            nl.append(lol[-1][j] - lol[-1][j-1])
        
        tl = list(filter(lambda e: e!=0, nl))
        if len(tl)==0:
            done = True
        else:
            lol.append(nl)
    
    for i in range(len(lol)-1, 0, -1):
        lol[i-1].insert(0, lol[i-1][0]-lol[i][-0])
    return(lol[0][0])      

part1 = 0
part2 = 0
for line in input:
    a=line.split(' ')
    a = list(map(lambda e: int(e), a))
    part1 += solve(a)
    part2 += solve2(a)


print("part1:", part1)
print("part2:", part2)