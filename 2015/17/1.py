import sys
import itertools

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2015', '17')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def countways(target, containers):
    ret = 0
    for n_containers in range(len(containers)):
        for combination in itertools.combinations(containers, n_containers):
            if sum(combination) == target:
                ret += 1
    return ret

def countways_part2(target, containers):
    ret = [0] + [0] * len(containers)
    for n_containers in range(len(containers)):
        for combination in itertools.combinations(containers, n_containers):
            if sum(combination) == target:
                ret[n_containers] += 1
    for c in ret:
        if c == 0:
            next
        else:
            return c   

containers = []
for line in input:
    containers.append(int(line))

print("part 1:", countways(150, containers)) # 1304
print("part 2:", countways_part2(150, containers)) # 18