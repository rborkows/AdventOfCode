import sys
import time

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '12')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def walk(node, paths):
    if node == "end":
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
    if node == "end":
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
        tmp = []
        for p in paths_from_here:
            p.append(nextnode)
            solution.append(p)
        
    return solution

print("part 1", walk("start", input))

smallcaves = set()
for path in input:
    ca = path.split("-")
    for cave in ca:
        if cave != 'start' and cave != 'end' and cave[0].islower():
            smallcaves.add(cave)

unique_paths = set()
for smallcave in smallcaves:
    paths=walk2("start", smallcave, input)
    for path in paths:
        unique_paths.add(":".join(path))

print("part 2", len(unique_paths))
