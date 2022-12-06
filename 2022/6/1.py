import sys
import math

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '6')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

part1=0
part2=0
line = input[0]

for i in range(len(line)-4):
    buf = line[i:i+4]
    bufs = set(buf)
    if len(bufs) == 4:
        part1=i+4
        break

for i in range(len(line)-14):
    buf = line[i:i+14]
    bufs = set(buf)
    if len(bufs) == 14:
        part2=i+14
        break

print("part1:", part1)
print("part2:", part2)