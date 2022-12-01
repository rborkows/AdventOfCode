import sys


sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '1')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

elves = [0]
for line in input:
    if line != "":
        calories = int(line)
        elves[-1] += calories
    else:
        elves.append(0)

elves.sort()
print("part1:", elves[-1])
print("part2:", elves[-1] + elves[-2] + elves[-3])