import sys
from collections import deque

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2016', '8')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Board:
    def __init__(self, width = 50, height = 6) -> None:
        self.width = width
        self.height = height
        self.board = []
        for row in range(height):
            self.board.append(deque(['.'] * width))

    def display(self):
        for row in self.board:
            print("".join(row))

    def operation(self, str):
        a = str.split()
        if a[0] == "rect":
            b = a[1].split('x')
            self.rect(int(b[0]), int(b[1]))
        elif a[1] == "row":
            row = int(a[2].split("=")[1])
            amount = int(a[4])
            self.rot_row(row, amount)
        elif a[1] == "column":
            column = int(a[2].split("=")[1])
            amount = int(a[4])
            self.rot_col(column, amount)
        # self.display()

    def rect(self, columns, rows):
        for row in range(rows):
            for column in range(columns):
                self.board[row][column] = "#"
    
    def rot_row(self, row, amount):
        self.board[row].rotate(amount)
    
    def rot_col(self, col, amount):
        c = deque()
        for i in range(self.height):
            c.append(self.board[i][col])
        c.rotate(amount)
        for i in range(self.height):
            self.board[i][col] = c[i]
    
    def litcount(self):
        lit = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == "#":
                    lit += 1

        return lit

b = Board()
for line in input:
    b.operation(line)

b.display()

print("Part1:", b.litcount())