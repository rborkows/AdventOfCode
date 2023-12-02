import sys
import re
from collections import defaultdict

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2023', '2')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

part1=0
# 12 red cubes, 13 green cubes, and 14 blue cubes
cubes_in_play = {'red':12, 'green':13, 'blue':14}
def is_possible(reveal):
    cubes_revealed=reveal.split(',')
    cubes_revealed=list(map(lambda e: e.lstrip(), cubes_revealed))
    for cubes in cubes_revealed:
        (amount, colour) = cubes.split(' ')
        amount=int(amount)
        if amount > cubes_in_play[colour]:
            return False
    return True

part2=0
def power(reveals):
    game = defaultdict(int)
    power = 1
    for reveal in reveals:
        reveal = reveal.split(',')
        cubes_revealed = list(map(lambda e: e.lstrip(), reveal))
        for cubes in cubes_revealed:
            (amount, colour) = cubes.split(' ')
            amount=int(amount)
            if game[colour] < amount:
                game[colour] = amount
    for colour in game:
        power *= game[colour]
    return power

for line in input:
    a=line.split(' ')
    game_id = int(a[1][:-1])
    a=line.split(':')
    reveals=a[1].split(';')
    possibles = list(map(is_possible, reveals))
    if all(possibles):
        part1 += game_id
    part2 += power(reveals)
print("part1: ", part1)
print("part2: ", part2)