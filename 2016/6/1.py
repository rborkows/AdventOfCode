import sys
from collections import Counter

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2016', '6')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

columns = []
for c in input[0]:
    columns.append(Counter())

for line in input:
    for i,c in enumerate(line):
        columns[i].update(c)

part1 = "".join([ c.most_common(1)[0][0] for c in columns ])
part2 = "".join([ c.most_common()[-1][0] for c in columns ])
print("Part1:", part1)
print("Part2:", part2)
