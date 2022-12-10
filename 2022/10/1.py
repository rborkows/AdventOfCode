import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '10')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

part1=0
part2=0
cycle = 1
X = 1
ax = [0]
for line in input:
    a=line.split()
    if len(a) == 1: # noop
        ax.append(X)
        cycle += 1
    else:
        ax.append(X)
        cycle += 1
        ax.append(X)
        cycle += 1
        X += int(a[1])


for cycle in [20,60,100,140,180,220]:
    part1 += cycle * ax[cycle]

print("part1:", part1) # 13520

line = ""
col = 0
for cycle in range(1,len(ax)):
    X = ax[cycle]
    if col == X-1 or col == X or col == X+1:
        line += "#"
    else:
        line += "."
    col += 1
    #print(cycle,X,line)
    if len(line) == 40:
        print(line)
        line = ""
        col = 0
    
# PGPHBEAB 
