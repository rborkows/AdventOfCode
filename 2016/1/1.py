import sys
import string
from collections import defaultdict

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2016', '1')
input = fetcher.fetch(rstrip=True, commasplit=True, small=False)

class Turtle:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.bearing = 0
        self.visited = defaultdict(int)
        self.visited[(0,0)] = 1
        self.firstcross = None
    
    def step(self, instruction):
        turn = instruction[0]
        magnitude = int(instruction[1:])
        if turn == 'R':
            self.bearing += 90
        elif turn == 'L':
            self.bearing -= 90
        if self.bearing < 0:
            self.bearing = 270
        elif self.bearing == 360:
            self.bearing = 0
        
        if self.bearing == 0:
            self.move_y(magnitude, 1)
        elif self.bearing == 90:
            self.move_x(magnitude, 1)
        elif self.bearing == 180:
            self.move_y(magnitude, -1)
        elif self.bearing == 270:
            self.move_x(magnitude, -1)

        ret = False
        if (self.x, self.y) in self.visited:
            ret = True

        # print(instruction, self.x, self.y, self.visited)

        return ret

    def move_y(self, magnitude, step):
        for m in range(magnitude):
            self.y += step
            if (self.x, self.y) in self.visited and self.firstcross == None:
                self.firstcross = (self.x, self.y)
            self.visited[(self.x, self.y)] += 1

    def move_x(self, magnitude, step):
        for m in range(magnitude):
            self.x += step
            if (self.x, self.y) in self.visited and self.firstcross == None:
                self.firstcross = (self.x, self.y)
            self.visited[(self.x, self.y)] += 1

    def manhattan_distance(self, x, y):
        return abs(x) + abs(y)

turtle = Turtle()

for step in input[0]:
    step = step.lstrip()
    turtle.step(step)
    
print("part1:", turtle.manhattan_distance(turtle.x, turtle.y))
print("part2:", turtle.manhattan_distance(turtle.firstcross[0], turtle.firstcross[1]))
