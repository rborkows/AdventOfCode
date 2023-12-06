import sys
import re


sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2023', '6')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)


def race(time, distance):
    races_won = 0
    for hold in range(1,time):
        remaining = time - hold
        speed = hold
        if (speed * remaining) > distance:
            races_won += 1
    return races_won

times = re.sub(r"\ +", " ", input[0]).split(" ")[1:]
distances = re.sub(r"\ +", " ", input[1]).split(" ")[1:]
times = list(map(lambda e: int(e), times))
distances = list(map(lambda e: int(e), distances))

part1 = 1
for i in range(len(times)):
    part1 *= race(times[i], distances[i])
print("part1:", part1)

time = int(re.sub(r"\ +", "", input[0]).split(":")[1])
distance = int(re.sub(r"\ +", "", input[1]).split(":")[1])
print("part2:", race(time, distance))