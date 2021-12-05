import unittest
from collections import Counter

class solutionTest(unittest.TestCase):
    def setUp(self):
        self.santa = Santa()
        self.team = Team(2)

    def test_part1_case1(self):
        self.santa.deliver('>')
        self.assertEqual(2, self.santa.houses_delivered_to())
    
    def test_part1_case2(self):
        self.santa.deliver('^>v<')
        self.assertEqual(4, self.santa.houses_delivered_to())

    def test_part1_case3(self):
        self.santa.deliver('^v^v^v^v^v')
        self.assertEqual(2, self.santa.houses_delivered_to())
    
    def test_part2_case1(self):
        self.team.deliver('^v')
        self.assertEqual(3, self.team.houses_delivered_to())

    def test_part2_case2(self):
        self.team.deliver('^>v<')
        self.assertEqual(3, self.team.houses_delivered_to())

    def test_part2_case3(self):
        self.team.deliver('^v^v^v^v^v')
        self.assertEqual(11, self.team.houses_delivered_to())


class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.delivered = Counter([f"{self.x}:{self.y}"])

    def deliver(self, directions):        
        for direction in directions.rstrip():
            self.move(direction)

    def move(self, direction):
        if direction == '^':
            self.y += 1
        elif direction == 'v':
            self.y -= 1
        elif direction == '<':
            self.x -= 1
        elif direction == '>':
            self.x += 1
        else:
            raise ValueError
        self.delivered.update([f"{self.x}:{self.y}"])

    def houses_delivered_to(self):
        return(len(self.delivered.keys()))

class Team:
    def __init__(self, size):
        self.santas = []
        for x in range(size):
            self.santas.append(Santa())

    def deliver(self, directions):
        active_santa = 0
        for direction in directions:
            self.santas[active_santa].move(direction)
            active_santa = (active_santa + 1 ) % len(self.santas)
    
    def houses_delivered_to(self):
        total_delivered = Counter()
        for santa in self.santas:
            total_delivered.update(santa.delivered)
        return(len(total_delivered.keys()))
        
#unittest.main()

with open("AdventOfCode/2015/3/input.txt") as f:
    directions = f.readline()

santa = Santa()
team = Team(2)
santa.deliver(directions)
part1 = santa.houses_delivered_to()
team.deliver(directions)
part2 = team.houses_delivered_to()
print(f"part1: {part1}")
print(f"part2: {part2}")
