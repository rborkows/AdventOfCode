import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '9')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

map_list = []
for line in input:
    row = []
    for c in line:
        row.append(int(c))
    map_list.append(row)

class Map:
    def __init__(self, map) -> None:
        self.map = map
        self.dim_rows = len(map)
        self.dim_cols = len(map[0])

    def score_lowspots(self):
        lowspots = self.find_lowspots()
        lowspots = [ self.map[p[0]][p[1]] for p in lowspots ]
        lowspots = [ p+1 for p in lowspots ]
        return sum(lowspots)

    def find_lowspots(self):
        lowspots = []
        for row in range(self.dim_rows):
            for col in range(self.dim_cols):
                point = self.map[row][col]
                neighbours = self.neighbours(row,col)
                neighbour_heights = [ self.map[p[0]][p[1]] for p in neighbours ]
                if point < min(neighbour_heights):
                    lowspots.append([row,col])            
        return lowspots

    def flood_basin(self, row, col):
        if self.map[row][col] == 9:
            return 0
        self.map[row][col] = 9
        ret = 1
        for n in self.neighbours(row, col):
            ret += self.flood_basin(n[0], n[1])
        return ret

    def neighbours(self, row,col):
        ret = []
        for n in [[-1, 0], [1, 0], [0, -1], [0, 1]]:        
            nrow = n[0] + row
            ncol = n[1] + col
            if nrow >= 0 and nrow < self.dim_rows and ncol >= 0 and ncol <self.dim_cols:
                ret.append([nrow, ncol])
        return ret

m = Map(map_list)
print("part1:", m.score_lowspots()) # 591

lowspots = m.find_lowspots()
basins = [ m.flood_basin(p[0], p[1]) for p in lowspots]
basins.sort(reverse=True)
print("part2:", basins[0] * basins[1] * basins[2]) # 1113424