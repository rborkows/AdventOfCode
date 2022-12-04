import sys
import math

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '4')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

part1 = 0
part2 = 0
for line in input:
    a=line.split(',')
    r1 = a[0].split('-')
    r2 = a[1].split('-')
    r1 = [ int(e) for e in r1 ]
    r2 = [ int(e) for e in r2 ]
    if r1[0] >= r2[0] and r1[1] <= r2[1] or r2[0] >= r1[0] and r2[1] <= r1[1]:
        part1 += 1

    if (r1[0] >= r2[0] and r1[0] <= r2[1] or r2[0] >= r1[0] and r2[0] <= r1[1]) or (r1[1] >= r2[0] and r1[1] <= r2[1] or r2[1] >= r1[0] and r2[1] <= r1[1]):
            part2 +=1
            
print("part1:", part1)
print("part2:", part2)