def part1(crabs):
    solutions = []
    for p in range(min(crabs), max(crabs) + 1):
        fuel_used = 0
        for crab in crabs:
            fuel_used += abs(crab - p)
        solutions.append(fuel_used)
    return min(solutions)

def sum_progression(n):
    return int((n/2) * (2 + (n - 1)))

def part2(crabs):
    solutions = []
    for p in range(min(crabs), max(crabs) + 1):
        fuel_used = 0
        for crab in crabs:
            distance = abs(crab - p)
            fuel_used += sum_progression(distance)
        solutions.append(fuel_used)
    return min(solutions)

with open("advent_2021/7/input.txt", "r") as f:
    crabs = f.readline().rstrip()
#crabs = "16,1,2,0,4,2,7,1,2,14"
crabs = crabs.split(',')
crabs = [ int(n) for n in crabs ]
print(part2(crabs))