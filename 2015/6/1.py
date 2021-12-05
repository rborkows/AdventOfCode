import re
from enum import Enum, auto
import sys

class Display:
    ON = auto()
    OFF = auto()
    TOGGLE = auto()

    def __init__(self, dimension = 1000) -> None:
        self.lights = []
        for row in range(dimension):
            self.lights.append([False] * dimension )
        
    def _parse_coordinate(self, coordinate: str):
        coordinate = coordinate.split(',')
        coordinate = [ int(n) for n in coordinate ]
        return coordinate

    def _parse_corners(self, corner1: str, corner2: str):
        corner1 = self._parse_coordinate(corner1)
        corner2 = self._parse_coordinate(corner2)
        return [corner1, corner2]

    def _change_light_state(self, x, y, operation):
        if operation == self.ON:
            self.lights[x][y] = True
        elif operation == self.OFF:
            self.lights[x][y] = False
        else:
            self.lights[x][y] = not self.lights[x][y]

    def _scan_rectangle(self, ul, lr, operation):
        for x in range(ul[0], lr[0]+1):
            for y in range(ul[1], lr[1]+1):
                self._change_light_state(x, y, operation)

    def turn_off(self, corner1: str, corner2: str):
        [ul, lr] = self._parse_corners(corner1, corner2)
        self._scan_rectangle(ul, lr, self.OFF)

    def turn_on(self, corner1: str, corner2: str):
       
        [ul, lr] = self._parse_corners(corner1, corner2)
        self._scan_rectangle(ul, lr, self.ON)

    def toggle(self, corner1: str, corner2: str):
        [ul, lr] = self._parse_corners(corner1, corner2)
        self._scan_rectangle(ul, lr, self.TOGGLE)

    def display(self):
        for row in self.lights:
            print(row)

    def count_lit(self):
        lit = 0
        for row in self.lights:
            for light in row:
                if light:
                    lit += 1
        return lit

class Display2(Display):
    def __init__(self, dimension = 1000) -> None:
        self.lights = []
        for row in range(dimension):
            self.lights.append([0] * dimension )

    def _change_light_state(self, x, y, operation):
        if operation == self.ON:
            self.lights[x][y] += 1
        elif operation == self.OFF:
            self.lights[x][y] -= 1
            if self.lights[x][y] < 0:
                self.lights[x][y] = 0  
        else:
            self.lights[x][y] += 2

    def count_lit(self):
        lit = 0
        for row in self.lights:
            for light in row:
                lit += light
        return lit


lights = Display()  # for part 1
lights = Display2() # for part 2

pattern = r'^(.*)\s(\d+,\d+) through (\d+,\d+)'
matcher = re.compile(pattern)
with open("AdventOfCode/2015/6/input.txt", "r") as f:
    for line in f:
        result = matcher.match(line.rstrip())
        if result.group(1) == "turn off":
            lights.turn_off(result.group(2), result.group(3))
        elif result.group(1) == "turn on":
            lights.turn_on(result.group(2), result.group(3))
        else:
            lights.toggle(result.group(2), result.group(3))    

print(f"lights: {lights.count_lit()}")
