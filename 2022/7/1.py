import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '7')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

global part1
global part2
part1=[]
part2 = []

class Node:
    def __init__(self, name, parent=None, type='f', size=0):
        self.name = name
        self.type = type
        self.size = size
        self.files = []
        self.children = []
        self.parent = parent

    def mkdir(self, name):
        self.children.append(Node(name, self, type='d'))

    def mkfile(self, name, size):
        self.files.append(Node(name, self, type='f', size=size))

    def walk(self):
        total = sum([e.size for e in self.files])
        for child in self.children:
            total += child.walk()
        #print("me:", self.name, " files:", [ e.name for e in self.files ], " total:", total)
        
        if(total < 100000):
            part1.append(total)
        if(total >= 2036703):
            part2.append(total)
        return total
        
        

root = Node("/", parent=None, type='d')
cwd = root


for line in input:
    a = line.split()
    if a[0]=='$':
        if a[1] == 'cd':
            if a[2] == '/':
                cwd = root
            elif a[2] == '..':
                if cwd.parent != None:
                    cwd = cwd.parent
            else:
                child = list(filter (lambda dir: dir.name == a[2], cwd.children))
                cwd = child[0]
                
        if a[1] == 'ls':
            pass
    else:
        if a[0] == 'dir':
            cwd.mkdir(a[1])
        elif a[0].isnumeric:
            cwd.mkfile(a[1], int(a[0]))

total = root.walk()
print("total:", total)
free = 70000000 - total
print("free:", free)
required = 30000000 - free
print("required:", required) # use this value in line 38


print("part1:", sum(part1))

part2.sort()
print("part2:", part2[0])