import sys
from collections import deque
from collections import defaultdict

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '17')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Rock:
    def __init__(self, rock_type) -> None:
        self.left_gap = 2
        if rock_type == 0:
            self.shape = deque()
            self.shape.append(deque([0,0,1,1,1,1,0]))
            self.height = 1
            self.right_gap = 1
        elif rock_type == 1:
            self.shape = deque()
            self.shape.append(deque([0,0,0,1,0,0,0]))
            self.shape.append(deque([0,0,1,1,1,0,0]))
            self.shape.append(deque([0,0,0,1,0,0,0]))
            self.height = 3
            self.right_gap = 2
        elif rock_type == 2:
            self.shape = deque()
            self.shape.append(deque([0,0,0,0,1,0,0]))
            self.shape.append(deque([0,0,0,0,1,0,0]))
            self.shape.append(deque([0,0,1,1,1,0,0]))
            self.height = 3
            self.right_gap = 2
        elif rock_type == 3:
            self.shape = deque()
            self.shape.append(deque([0,0,1,0,0,0,0]))
            self.shape.append(deque([0,0,1,0,0,0,0]))
            self.shape.append(deque([0,0,1,0,0,0,0]))
            self.shape.append(deque([0,0,1,0,0,0,0]))
            self.height = 4
            self.right_gap = 4
        elif rock_type == 4:
            self.shape = deque()
            self.shape.append(deque([0,0,1,1,0,0,0]))
            self.shape.append(deque([0,0,1,1,0,0,0]))
            self.height = 2
            self.right_gap = 3
        else:
            print("Invalid rock type")
            exit(1)
        self.y = self.height
        
    def down(self):
        self.y -= 1
    
    def up(self):
        self.y += 1
    
    def left(self):
        if self.left_gap > 0:
            self.left_gap -= 1
            self.right_gap += 1
            for row in self.shape:
                row.rotate(-1)
        
    def right(self):
        if self.right_gap > 0:
            self.right_gap -= 1
            self.left_gap += 1
            for row in self.shape:
                row.rotate(1)

class Chamber:
    def __init__(self) -> None:
        self.shape = deque()
        self.floor = 0
        self.trimmed = 0
        self.rock = None
        self.height=len(self.shape)
        self.surface_minumum = 0

    def add_rock(self, rock):
        self.rock = rock
        for n in range(3 + self.rock.height):
            self.shape.append(deque([0] * 7))
        self.height=len(self.shape)

    def display(self):
        if self.rock != None:
            self.merge_rock()
        for row in range(len(self.shape)-1, -1, -1):
            line = "|"
            for c in self.shape[row]:
                if c==0:
                    line += "."
                elif c==1:
                    line += "@"
                elif c==10:
                    line += "#"
                else:
                    line += "!"
            line += "|"
            print(line)
        print("+-------+\n")
        if self.rock != None:
            self.unmerge_rock()
    
    def merge_rock(self, final=False):
        for row_i in range(len(self.rock.shape)):
            for col_i in range(7):
                if final:
                    self.shape[self.height-self.rock.height+self.rock.y-row_i-1][col_i] += 10 * self.rock.shape[row_i][col_i]
                else:
                    self.shape[self.height-self.rock.height+self.rock.y-row_i-1][col_i] += self.rock.shape[row_i][col_i]

    def unmerge_rock(self):
        for row_i in range(len(self.rock.shape)):
           for col_i in range(7):
                self.shape[self.height-self.rock.height+self.rock.y-row_i-1][col_i] -= self.rock.shape[row_i][col_i]

    def rock_collision(self):
        for row_i in range(len(self.rock.shape)):
            for col_i in range(7):
                if self.shape[self.height-self.rock.height+self.rock.y-row_i-1][col_i] + self.rock.shape[row_i][col_i] > 10:
                    return True
        return False

    def push(self, direction):
        if direction == "<":
            self.rock.left()
            if self.rock_collision():
                self.rock.right()
        elif direction == ">":
            self.rock.right()
            if self.rock_collision():
                self.rock.left()

    def gravity(self):
        self.rock.down()
        if self.rock.y == -(self.height - 1) or self.rock_collision():
            self.rock.up()
            self.merge_rock(final=True)
            self.rock = None
            self.trim()

    def tick(self, direction):
        self.push(direction)
        #self.display()
        self.gravity()
        
    def trim(self):
        empty_row = deque([0] * 7)

        while self.shape[-1] == empty_row:
            self.shape.pop()
    
    def rockline(self):
        self.height=len(self.shape)
        return self.height

    def get_surface(self):
        surface = [0] * 7
        for row in range(self.surface_minumum, len(self.shape)):
            for i in range(7):
                if self.shape[row][i] > 0:
                    surface[i] = row
        minimum = min(surface)
        self.surface_minumum = max(self.surface_minumum, minimum)
        surface = [ e - minimum for e in surface ]
        return tuple(surface)

part1=0
part2=0
jet_i = 0
chamber = Chamber()
jets = input[0]
surfaces = defaultdict(list)

factor1 = 0
factor2 = 0
rock_count = 0
for rock_count in range(5000):
    chamber.add_rock(Rock(rock_count % 5))
    while chamber.rock != None:
        chamber.tick(jets[jet_i % len(jets)])
        jet_i += 1
    #chamber.display()
    surface = chamber.get_surface()
    #print("surface:", surface)
    #print("shape:", chamber.shape)
    if surface is not None:
        surface_tuple = (rock_count % 5, surface)
        surfaces[surface_tuple].append((rock_count, chamber.rockline()))
        if len(surfaces[surface_tuple]) == 3 and rock_count > 2000:
            #print("x:", surfaces[surface_tuple])
            point1 = surfaces[surface_tuple][0]
            point2 = surfaces[surface_tuple][1]
            point3 = surfaces[surface_tuple][2]
            if point3[0] - point2[0] == point2[0] - point1[0]:
                factor1 = point2[0] - point1[0]
                factor2 = point2[1] - point1[1]
                break;
#rock_count += 1
#print("f1:", factor1)
#print("f2:", factor2)   
#part1
(multiplier, remainder) = divmod(2021,factor1)
for key in surfaces.keys():
    if key[0] == 2021 % 5:
        for e in surfaces[key]:
            if e[0] == remainder:
                part1 = multiplier * factor2 + e[1]
                #print("e:", e)
                break

#part2
(multiplier, remainder) = divmod(10**12 - 1,factor1)
for key in surfaces.keys():
    if key[0] == (10**12 - 1) % 5:
        for e in surfaces[key]:
            if e[0] == remainder:
                part2 = multiplier * factor2 + e[1]
                break

print("part1:", part1) # 3111
print("part2:", part2) # 1526744186042
