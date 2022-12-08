import sys
from math import prod

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '8')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Forest:
    def __init__(self, heights):
        self.heights = heights
        self.dim = len(heights)
        self.visible = set()
        self.max_beauty = 0
        self.calculate_visibility()
        self.calculate_max_beauty()

    def beauty_spot(self, r, c):
        subject_height = self.heights[r][c]
        beauty = []

        # looking up
        visible = 0
        for row in range(r-1,-1,-1):
            if self.heights[row][c] < subject_height:
                visible += 1
            elif self.heights[row][c] >= subject_height:
                visible += 1
                break
        beauty.append(visible)

        #looking left
        visible = 0
        for col in range(c-1, -1, -1):
            if self.heights[r][col] < subject_height:
                visible += 1
            elif self.heights[r][col] >= subject_height:
                visible += 1
                break  
        beauty.append(visible)

        # looking right
        visible = 0
        for col in range(c+1,self.dim):
            if self.heights[r][col] < subject_height:
                visible += 1
            elif self.heights[r][col] >= subject_height:
                visible += 1
                break
        beauty.append(visible)

        # looking down
        visible = 0
        for row in range(r+1,self.dim):
            if self.heights[row][c] < subject_height:
                visible += 1
            elif self.heights[row][c] >= subject_height:
                visible += 1
                break
        beauty.append(visible)

        return prod(beauty)

    def calculate_max_beauty(self):
        self.max_beauty = 0
        for row in range(self.dim):
            for col in range(self.dim):
                bs = self.beauty_spot(row, col)
                if bs > self.max_beauty:
                    self.max_beauty = bs

    def calculate_visibility(self):
        # edges
        for row in range(self.dim):
            self.visible.add(((row,0)))
            self.visible.add((row,self.dim-1))
        for col in range(self.dim):
            self.visible.add((0,col))
            self.visible.add((self.dim-1,col))

        # rows
        for row in range(1,self.dim-1):
            # left to right
            highest = self.heights[row][0]
            for col in range(1,self.dim-1):
                if self.heights[row][col] > highest:
                    highest = self.heights[row][col]
                    self.visible.add((row,col))
            # right to left
            highest = self.heights[row][-1]
            for col in range(self.dim-1,0,-1):
                if self.heights[row][col] > highest:
                    highest = self.heights[row][col]
                    self.visible.add((row,col))

        # columns
        for col in range(1,self.dim-1):
            # top to bottom
            highest = self.heights[0][col]
            for row in range(1,self.dim-1):
                if self.heights[row][col] > highest:
                    highest = self.heights[row][col]
                    self.visible.add((row,col))
            # bottom to top
            highest = self.heights[-1][col]
            for row in range(self.dim-1,0,-1):
                if self.heights[row][col] > highest:
                    highest = self.heights[row][col]
                    self.visible.add((row,col))

    def visible_count(self):
        return len(self.visible)

forest = []
for line in input:
    forest.append(list(line))
    forest[-1] = [ int(e) for e in forest[-1]]

f = Forest(forest)

part1 = f.visible_count()
part2 = f.max_beauty
print("part1:", part1)
print("part2:", part2)
