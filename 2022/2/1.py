import sys
import math

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '2')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

#A X Rock        1
#B Y Paper       2
#C Z Scissors    3

# X lose
# Y draw
# Z win

shapescore = {'X':1, 'Y':2, 'Z':3}

part1=0
part2=0

for line in input:
    a = line.split()
    part1 += shapescore[a[1]]
    if a[0] == 'A': # rock
        if a[1] == 'X':
            part1 += 3
            part2 += 3
        elif a[1] == 'Y':
            part1 += 6
            part2 += 1 + 3
        elif a[1] == 'Z':
            part1 += 0
            part2 += 2 + 6
    elif a[0] == 'B': # paper
        if a[1] == 'X':
            part1 += 0
            part2 += 1
        elif a[1] == 'Y':
            part1 += 3
            part2 += 2 + 3
        elif a[1] == 'Z':
            part1 += 6
            part2 += 3 + 6
    elif a[0] == 'C': # scissors
        if a[1] == 'X':
            part1 += 6
            part2 += 2
        elif a[1] == 'Y':
            part1 += 0
            part2 += 3 + 3
        elif a[1] == 'Z':
            part1 += 3
            part2 += 1 + 6

print("part1:", part1)
print("part2:", part2)