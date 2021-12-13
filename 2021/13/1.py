import sys


sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '13')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Board:
    def __init__(self, points) -> None:
        self.points=points
        self.get_extent()
    
    def fold_up(self,y):
        new_points = set()
        for p in self.points:
            if p[1] < y:
                new_points.add(p)
            else:
                d = p[1] - y
                new_points.add((p[0], y-d))
        self.points = new_points
        self.get_extent()

    def fold_left(self, x):
        new_points = set()
        for p in self.points:
            if p[0] < x:
                new_points.add(p)
            else:
                d = p[0] - x
                new_points.add((x-d, p[1]))
        self.points = new_points
        self.get_extent()


    def display(self):
        for y in range(self.max_y+1):
            line = ""
            for x in range(self.max_x+1):
                if (x, y) in self.points:
                    line += "#"
                else:
                    line += "."
            print(line)
    
    def get_extent(self):
        self.max_x = max([e[0] for e in self.points])
        self.max_y = max([e[1] for e in self.points])

separator = input.index("")
points = set()
for point in input[:separator]:
    x,y = point.split(",")
    points.add((int(x), int(y)))

folds = input[separator+1:]

b = Board(points)
fold_count = 0
part1 = 0
for fold in folds:
    dir,axis = fold.split("=")
    axis = int(axis)
    if "x" in dir:
        b.fold_left(axis)
    else:
        b.fold_up(axis)
    fold_count += 1
    if fold_count == 1:
        part1 = len(b.points)
    
print("part1: ", part1)
b.display()