import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '15')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
        self._hash = hash(f"{self.x}:{self.y}")

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self._hash == other._hash

    def __hash__(self):
        return self._hash

class Sensor:
    def __init__(self, line):
        a=line.split()
        
        self.my_position=Point(int(a[2].split("=")[1][:-1]), int(a[3].split("=")[1][:-1]))
        self.beacon_position=Point(int(a[8].split("=")[1][:-1]), int(a[9].split("=")[1]))
        self.distance_to_beacon = self.my_position.manhattan_distance(self.beacon_position)

    def __str__(self):
        return f"me:{self.my_position} distance:{self.distance_to_beacon}"

    def inrange(self, point):
        dist = self.my_position.manhattan_distance(point)
        return dist <= self.distance_to_beacon

    def range_at_row(self, row):
        dist = abs(self.my_position.y - row)
        h_width = self.distance_to_beacon - dist
        if h_width >= 0:
            return (self.my_position.x - h_width, self.my_position.x + h_width)
        else:
            return (None, None)

def merge_ranges(ranges):
    ranges = list(filter(lambda e: e[0] != None, ranges))
    ranges.sort(key=lambda e: e[0])
    merged = [ ranges.pop(0) ] 
    for r in ranges:
        prev = merged[-1]
        if r[0] <= prev[1]:
            merged[-1] = ( prev[0], max(r[1], prev[1]))


    return merged

part1=0
part2=0
sensors = []
for line in input:
    s=Sensor(line)
    sensors.append(s)

ranges = [ s.range_at_row(2000000) for s in sensors ]
ranges = merge_ranges(ranges)
part1 = ranges[0][1] - ranges[0][0]

for y in range(4000001):
    ranges = [ s.range_at_row(y) for s in sensors ]
    ranges = merge_ranges(ranges)
    if len(ranges) > 1 or ranges[0][0] > 0 or ranges[0][1] < 4000000:
        part2 = (ranges[0][1]+1) * 4000000 + y
        print(y, ranges)
        break




print("part1:", part1) # 4665948
print("part2:", part2) # 13543690671045