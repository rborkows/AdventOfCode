import sys
import re

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2015', '16')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

characteristics={
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}
sues = []
#                        1     2      3      4      5      6      7
pat = re.compile(r"^Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)")
for line in input:
    m = re.match(pat, line)
    sue = m.group(1)
    ch = {}
    for i in range(2,8,2):
        ch[m.group(i)] = int(m.group(i+1))
    sues.append(ch)

for i,sue in enumerate(sues):
    matches = [ sue[ch] == characteristics[ch] for ch in sue.keys() ]
    if all(matches):
        print("part 1:", i+1)
        break

for i,sue in enumerate(sues):
    matches = []
    for ch in sue.keys():
        if ch in ["cats", "trees"]:
            matches.append(sue[ch] > characteristics[ch])
        elif ch in ["pomeranians", "goldfish"]:
            matches.append(sue[ch] < characteristics[ch])
        else:
            matches.append(sue[ch] == characteristics[ch])
    if all(matches):
        print("part 2:", i+1)
