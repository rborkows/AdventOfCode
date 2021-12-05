import unittest
import sys

class solutionTest(unittest.TestCase):
    def setUp(self):
        self.wrapper = Wrapper()

    def test_part1_case1(self):
        self.assertEqual(58, self.wrapper.paper_required('2x3x4'))
    
    def test_part1_case2(self):
        self.assertEqual(43, self.wrapper.paper_required('1x1x10'))

class Box:
    def __init__(self, dimensions):
        self.dimensions = dimensions.split('x')
        self.dimensions = [ int(n) for n in self.dimensions]
        self.dimensions.sort()
        

    def smallest_side_area(self):
        return self.dimensions[0] * self.dimensions[1]

    def surface_area(self):
        return 2*(self.dimensions[0] * self.dimensions[1]) + 2*(self.dimensions[0] * self.dimensions[2]) + 2*(self.dimensions[1] * self.dimensions[2])


class Wrapper:
    def __init__(self):
        pass

    def paper_required(self, dimensions: str):
        box = Box(dimensions.rstrip())
        return box.surface_area() + box.smallest_side_area()
        
#unittest.main()

wrapper = Wrapper()
with open("AdventOfCode/2015/2/input.txt") as f:
    sum = 0
    for box_dimensions in f:
        sum += wrapper.paper_required(box_dimensions)

print(f"part1:", sum)