import sys
import re
from collections import Counter

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2016', '4')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def checksum(str):
    c=Counter(str)
    l = list(c.items())
    l.sort(key=lambda e: (-e[1], e[0]))
    l = [ e[0] for e in l ]
    l = l[:5]
    l = "".join(l)
    
    return l

def rotate(str, n):
    a = [ chr((ord(c)-ord('a')+n)%26+ord('a')) for c in str ]
    return "".join(a)

pat = "([a-z\-]+)(\d+)\[([a-z]+)\]"
prog = re.compile(pat)

part1 = 0
part2 = 0
for line in input:
    m = prog.match(line)
    roomchars = m.group(1).replace("-", "")
    cksum = checksum(roomchars)
    if cksum == m.group(3):
        part1 += int(m.group(2))
        decrypted = rotate(roomchars, int(m.group(2)))
        if "north" in decrypted:
            part2 = m.group(2)
    
print("Part1:", part1)
print("Part2:", part2)
