class Line:
    def __init__(self, p1, p2):
        self.p1 = p1.split(',')
        self.p1 = [ int(n) for n in self.p1 ]
        self.p2 = p2.split(',')
        self.p2 = [ int(n) for n in self.p2 ]

    def is_horizontal(self) -> bool:
        return self.p1[1] == self.p2[1]

    def is_vertical(self) -> bool:
        return self.p1[0] == self.p2[0]

    def __str__(self) -> str:
        return f"{self.p1} -> {self.p2}"
        
class Board:
    def __init__(self, dimension):
        self.board = []
        for rows in range(dimension):
            self.board.append([0] * dimension)

    def render_line(self, line: Line):
        if line.is_horizontal():
            if line.p1[0] < line.p2[0]:
                start = line.p1
                end = line.p2
            else:
                start = line.p2
                end = line.p1
            y = start[1]
            for x in range(start[0], end[0]+1):
                self.board[x][y] += 1
        elif line.is_vertical():
            if line.p1[1] < line.p2[1]:
                start = line.p1
                end = line.p2
            else:
                start = line.p2
                end = line.p1
            x = start[0]
            for y in range(start[1], end[1]+1):
                self.board[x][y] += 1
        else:
            if line.p1[0] < line.p2[0]:
                start = line.p1
                end = line.p2
            else:
                start = line.p2
                end = line.p1
            if start[1] < end[1]:
                slope = 1
            else:
                slope = -1
            y = start[1]
            for x in range(start[0], end[0]+1):
                self.board[x][y] += 1
                y += slope
            
    def danger_zones(self):
        danger = 0
        for y in range(1000):
            for x in range(1000):
                if self.board[x][y] >= 2:
                    danger += 1
        return(danger)

    def display(self):
        for row in self.board:
            print(row)

board = Board(1000)
with open("advent_2021/5/input.txt", "r") as f:
    h_or_v_lines = []
    d_lines = []
    for line in f:
        (p1, _, p2) = line.split()
        l = Line(p1, p2)
        if l.is_horizontal() or l.is_vertical():
            h_or_v_lines.append(l)
        else:
            d_lines.append(l)

for line in h_or_v_lines:
    board.render_line(line)
print(f"part1: {board.danger_zones()}")

for line in d_lines:
    board.render_line(line)
print(f"part2: {board.danger_zones()}")
