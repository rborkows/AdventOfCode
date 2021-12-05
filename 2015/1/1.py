import unittest

class solutionTest(unittest.TestCase):
    def setUp(self):
        self.solver = Solver()

    def test_case1(self):
        self.assertEqual(0, self.solver.part1('(())'))
    
    def test_case2(self):
        self.assertEqual(0, self.solver.part1('()()'))

    def test_case3(self):
        self.assertEqual(3, self.solver.part1('((('))

    def test_case4(self):
        self.assertEqual(3, self.solver.part1('(()(()('))

    def test_case5(self):
        self.assertEqual(3, self.solver.part1('))((((('))

    def test_case6(self):
        self.assertEqual(-1, self.solver.part1('())'))

    def test_case7(self):
        self.assertEqual(-1, self.solver.part1('))('))

    def test_case8(self):
        self.assertEqual(-3, self.solver.part1(')))'))

    def test_case8(self):
        self.assertEqual(-3, self.solver.part1(')())())'))

    def test_part2_case1(self):
        self.assertEqual(1, self.solver.part2(')'))

    def test_part2_case2(self):
        self.assertEqual(5, self.solver.part2('()())'))

class Solver:
    def __init__(self):
        self.floor = 0

    def part1(self, buttonsequence):
        for c in buttonsequence:
            if c == '(':
                self.floor += 1
            elif c == ')':
                self.floor -= 1
        return self.floor

    def part2(self, buttonsequence):
        for p, c in enumerate(buttonsequence):
            if c == '(':
                self.floor += 1
            elif c == ')':
                self.floor -= 1
            if self.floor == -1:
                return p+1
            
        raise NeverGotToBasement


#unittest.main()

with open("AdventOfCode/2015/1/input.txt") as f:
    sequence = f.readline()

sequence = sequence.rstrip()
solver = Solver()
print("part1:", solver.part1(sequence))
solver.floor = 0
print("part2: ", solver.part2(sequence))