import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '12')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def walk(node, paths):
    # print("At", node, paths)
    if node == "end":
        # print("Made it")
        return 1
    canreturn = node[0].isupper()
    mypaths = []
    nextpaths = []
    for path in paths:
        if node in path:
            mypaths.append(path)
            if canreturn:
                nextpaths.append(path)
        else:
            nextpaths.append(path)
    # print("nextpaths:", nextpaths)
    # print("mypaths", mypaths)
    if mypaths == []:
        return 0
    ret = 0
    for path in mypaths:
        p1, p2 = path.split("-")
        if p1 == node:
            nextnode = p2
        else:
            nextnode = p1
        ret += walk(nextnode, nextpaths)

    return ret

def walk2(node, specialsmall, paths):
    # print("At", node, paths)
    if node == "end":
        # print("Made it")
        return [[]]
    canreturn = node[0].isupper()
    if node == specialsmall:
        canreturn = True
        specialsmall = None
    mypaths = []
    nextpaths = []
    for path in paths:
        if node in path:
            mypaths.append(path)
            if canreturn:
                nextpaths.append(path)
        else:
            nextpaths.append(path)
    # print("nextpaths:", nextpaths)
    # print("mypaths", mypaths)
    if mypaths == []:
        return []
    solution = []
    for path in mypaths:
        p1, p2 = path.split("-")
        if p1 == node:
            nextnode = p2
        else:
            nextnode = p1
        paths_from_here = walk2(nextnode, specialsmall, nextpaths)
        # print("paths", paths_from_here, node)
        tmp = []
        for p in paths_from_here:
            # print("p", p)
            p.append(nextnode)
            solution.append(p)
        
    return solution

# print(input)
smallcaves = set()
for path in input:
    ca = path.split("-")
    for cave in ca:
        if cave != 'start' and cave != 'end' and cave[0].islower():
            smallcaves.add(cave)

# print("smallcaves:", smallcaves)
print("part1", walk("start", input))

# pathcount = 0
# for smallcave in smallcaves:
    # pathcount += walk2("start", smallcave, input)
part2 = []
for smallcave in smallcaves:
    print("smallcave", smallcave)
    paths=walk2("start", smallcave, input)
    for path in paths:
        if path not in part2:
            part2.append(path)

print(len(part2))
