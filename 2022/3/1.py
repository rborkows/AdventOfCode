import sys
import math

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '3')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def value(ch):
    if ord(ch) <= 90:
        return 27 + ord(ch) - ord('A')
    else:
        return 1 + ord(ch) - ord('a')


part1=0
for line in input:
    l = len(line)
    p1=line[:l//2]
    p2=line[l//2:]
    for c in p2:
        if c in p1:
            part1 += value(c)
            break

print("part1:", part1)

part2=0

groups = len(input)//3
for p in range(groups):
    for c in range(ord('a'), ord('z') + 1):
        if chr(c) in input[p*3] and chr(c) in input[p*3+1] and chr(c) in input[p*3+2]:
            part2 += value(chr(c))
    for c in range(ord('A'), ord('Z') + 1):
        if chr(c) in input[p*3] and chr(c) in input[p*3+1] and chr(c) in input[p*3+2]:
            part2 += value(chr(c))
        
print("part2:", part2)