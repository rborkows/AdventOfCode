import sys
import math

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '5')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

stacks_n = 9
stacks = []

for n in range(stacks_n):
    stacks.append([])

n=3
for line in input:
    n+=1
    if line =="":
        break
    for n in range(stacks_n):
        if len(line) < n*4+1:
            break
        if line[n*4+1] != " " and not line[n*4+1].isnumeric():
            stacks[n].append(line[n*4+1]) 

for line in input[10:]: # 5 for small
    a=line.split()
    count = int(a[1])
    source = int(a[3]) - 1
    destination = int(a[5]) - 1
    stacks[destination] = stacks[source][:count] + stacks[destination]
    stacks[source] = stacks[source][count:]
    
part2=""
for n in range(stacks_n):
    part2+=stacks[n][0]


print("part2:", part2)
