import sys
import re
from itertools import permutations

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2016', '3')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def isTriangle(shape):
    for i in permutations(range(3),3):
        if shape[i[0]] + shape[i[1]] <= shape[i[2]]:
            return False
    return True

pat = "^\s*(\d+)\s+(\d+)\s+(\d+)"
prog = re.compile(pat)

part1 = 0
shapes = []
for line in input:
    res = prog.match(line)
    if res:
        shape = [ res.group(1), res.group(2), res.group(3) ]
        shape = [ int(n) for n in shape ]
        shapes.append(shape)
        if isTriangle(shape):
            part1 += 1
        
print("Part1:", part1)

part2 = 0
for i in range(len(shapes)//3):
    for j in range(3): # across
        shape = []
        for k in range(3): # down
            shape.append(shapes[i*3 + k][j])
        if isTriangle(shape):
            part2 += 1

print("Part2:", part2)