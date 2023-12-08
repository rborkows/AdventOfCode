import sys
from math import lcm


sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2023', '8')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Node:
    def __init__(self, line) -> None:
        self.name = line[0:3]
        self.left = line[7:10]
        self.right = line[12:15]

    def child(self, direction):
        if direction == 'R':
            return self.right
        elif direction == 'L':
            return self.left
        else:
            print("Invalid direction")
    
    def __repr__(self) -> str:
        return f"Node: {self.name} {self.left} {self.right}"

directions = input[0]
input = input[2:]

nodes = {}
for line in input:
    node = Node(line)
    nodes[node.name] = node

curnode = nodes['AAA']
part1=0
while curnode.name != 'ZZZ':
    direction = directions[part1%len(directions)]
    
    curnode = nodes[curnode.child(direction)]
    part1 += 1
print("part1:", part1)

curnodes = []
for node in nodes:
    if nodes[node].name[2] == 'A':
        curnodes.append(node)
part2=0

cycles = []
for curnode in curnodes:
    step = 0
    while curnode[2] != 'Z':
        direction = directions[step%len(directions)]
        curnode = nodes[curnode].child(direction)
        step += 1
    cycles.append(step)

print("part2:", lcm(*cycles))