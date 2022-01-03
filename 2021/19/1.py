import sys
import numpy as np
from collections import defaultdict
import itertools

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '19')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Scanner:
    rot_x = np.array([[1,0,0], [0, 0, -1], [0, 1, 0]])
    rot_y = np.array([[0,0,1], [0,1,0], [-1,0,0]])
    rot_z = np.array([[0,-1,0], [1,0,0], [0,0,1]])
    def __init__(self, id) -> None:
        self.id = id
        self.beacons = []
        if self.id == 0:
            self.disoriented = False
            self.offset = np.array([0,0,0])
        else:
            self.disoriented = True
            self.offset = None
        
    def rotate_x(self):
        self.beacons = [ np.matmul(self.rot_x, e, e) for e in self.beacons ]

    def rotate_y(self):
        self.beacons = [ np.matmul(self.rot_y, e, e) for e in self.beacons ]
    
    def rotate_z(self):
        self.beacons = [ np.matmul(self.rot_z, e, e) for e in self.beacons ]
    
    def overlap_count(self, oriented_beacons): # return number of overlapping points for a given orientation
        offsets = self.get_offsets(oriented_beacons)
        return sorted(offsets.values())[-1]

    def get_offsets(self, oriented_beacons):
        offsets = defaultdict(int)
        for self_beacon in self.beacons:
            for oriented_beacon in oriented_beacons:
                # print(self_beacon, oriented_beacon, oriented_beacon - self_beacon)
                offsets[tuple(oriented_beacon - self_beacon)] += 1
        return offsets
                    
    def orient(self, oriented_beacons): # return True if successfully oriented
        best_overlap = 0
        
        for _ in self.rotations():
            overlaps=self.overlap_count(oriented_beacons)
            if overlaps > best_overlap:
                best_overlap = overlaps

        if best_overlap >= 2:
            for _ in self.rotations():
                overlaps=self.overlap_count(oriented_beacons)
                if overlaps == best_overlap:
                    self.disoriented = False
                    offsets = self.get_offsets(oriented_beacons)
                    best_offset = None
                    for offset in offsets.keys():
                        if offsets[offset] == best_overlap:
                            self.offset = np.array(offset)
                            return True

        return False

    def rotations(self):
        for r in range(4):
            self.rotate_y()
            yield True
        self.rotate_z()
        for r in range(4):
            self.rotate_x()
            yield True
        self.rotate_z()
        for r in range(4):
            self.rotate_y()
            yield True
        self.rotate_z()
        for r in range(4):
            self.rotate_x()
            yield True
        self.rotate_y()
        for r in range(4):
            self.rotate_z()
            yield True
        self.rotate_y()
        self.rotate_y()
        for r in range(4):
            self.rotate_z()
            yield True
        



scanners = []
for line in input:
    if "---" in line:
        a = line.split()
        scanners.append(Scanner(int(a[2])))
    elif len(line) > 0:
        a = line.split(",")
        a = [ int(n) for n in a ]
        scanners[-1].beacons.append(np.array(a))

oriented_beacons = scanners[0].beacons

while True:
    disoriented = list(filter(lambda scanner: scanner.disoriented == True, scanners))
    if len(disoriented) == 0:
        break
    for scanner in disoriented:
        if scanner.orient(oriented_beacons):
            for beacon in scanner.beacons:
                oriented_beacon = scanner.offset + beacon
                matches = [ np.array_equal(oriented_beacon,e) for e in oriented_beacons]
                if not any(matches):
                    oriented_beacons.append(oriented_beacon)

print("Part 1:", len(oriented_beacons))
distances = []
for pair in itertools.combinations(scanners,2):
    distance = np.absolute(pair[0].offset - pair[1].offset)
    distances.append(sum(distance))
print("Part 2:", max(distances)) # 8392 is too low