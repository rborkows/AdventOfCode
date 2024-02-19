import sys
import re
from itertools import permutations, combinations


sys.path.append("AdventOfCode/lib")
import adventutil


def expand(stars, expansion):
    expansion -= 1
    for star in stars:
        row = star[0]
        col = star[1]
        for empty_row in empty_rows:
            if row > empty_row:
                star[0] += expansion
        for empty_col in empty_cols:
            if col > empty_col:
                star[1] += expansion

def manhattan_distance(star1, star2):
    return abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])

fetcher = adventutil.InputFetcher('2023', '11')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

dim = len(input)
empty_cols = []
empty_rows = []
for row in range(dim):
    if not '#' in input[row]:
        empty_rows.append(row)
for col in range(dim):
    is_empty=True
    for row in range(dim):
        if input[row][col] == '#':
            is_empty = False
            break
    if is_empty:
        empty_cols.append(col)
n_rows = len(input)
stars = []
stars_2 = []
for row_n in range(n_rows):
    for col_n in range(len(input[row_n])):
        if input[row_n][col_n] == '#':
            stars.append([row_n,col_n])
            stars_2.append([row_n,col_n])

expand(stars, 2)
expand(stars_2, 1000000)

part1 = 0
for i in combinations(range(len(stars)), 2):
    part1 += manhattan_distance(stars[i[0]], stars[i[1]])

part2 = 0
for i in combinations(range(len(stars_2)), 2):
    part2 += manhattan_distance(stars_2[i[0]], stars_2[i[1]])

print("part1:", part1)
print("part2:", part2)