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
    p1=set(line[:l//2])
    p2=set(line[l//2:])
    part1 += value(list(p1&p2)[0])
    
print("part1:", part1) # 8349

part2=0
groups = len(input)//3
for p in range(groups):
    common = set(input[p*3]) & set(input[p*3+1]) & set(input[p*3+2])
    part2 += value(list(common)[0])
         
print("part2:", part2) # 2681