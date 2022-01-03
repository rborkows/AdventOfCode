import sys

sys.path.append("AdventOfCode/lib")
import adventutil
from collections import defaultdict

fetcher = adventutil.InputFetcher('2021', '15')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def walk(row,col,cave, memo={}):
    if (row,col) in memo:
        return memo[(row,col)]
    if row == len(cave)-1 and col == len(cave[0])-1:
        return cave[row][col]
    if row >= len(cave) or col >= len(cave[0]):
        return None
    else:
        d = walk(row+1, col, cave)
        r = walk(row, col+1, cave)
        # print(row, col, d, r)
        if d !=None and r!=None:
            memo[(row,col)] = min(r,d)
        elif d !=None:
            memo[(row,col)] = d
        else:
            memo[(row,col)] = r
        memo[(row,col)] += cave[row][col]

        return memo[(row,col)]


cave = []
for line in input:
    line = [ int(n) for n in line ]
    cave.append(line)


s=walk(0,0,cave)
s -= cave[0][0]
print("part 1:", s)
