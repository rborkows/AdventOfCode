import sys
import math

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2019', '1')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)


def fueluse(mass):
    return(math.floor(mass/3) - 2)

def fueluse2(mass):
    ret = 0
    fuel = fueluse(mass)
    ret = fuel
    while fuel > 5:
        fuel = fueluse(fuel)
        ret += fuel
    return(ret)
    
part1=0
part2=0
for line in input:
    part1 += fueluse(int(line))
    part2 += fueluse2(int(line))
print("part1:", part1)
print("part2:", part2)