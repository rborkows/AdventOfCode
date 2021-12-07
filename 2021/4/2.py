import os

class Board:
    def __init__(self):
        self.board = []
        self.won = False
        
    def addrow(self, r):
        r = [ int(n) for n in r.split() ]
        self.board.append(r)
        
    def display(self):
        for row in self.board:
            print(row)

    def check_horizontal(self, row):
        for col in range(5):
            if self.board[row][col] != None:
                return False
        return True

    def check_vertical(self, col):
        for row in range(5):
            if self.board[row][col] != None:
                return False
        return True

    def mark(self, n):
        match = False
        for row_n, row in enumerate(self.board):
            if n in row:
                match = True
                col_n = row.index(n)
                self.board[row_n][col_n] = None

                if self.check_horizontal(row_n) or self.check_vertical(col_n):
                    self.won = True
                    return True
                else:
                    return False
                
    def sum(self):
        ret = 0
        for row in self.board:
            for col in range(5):
                if row[col]:
                    ret += row[col]
        return ret

    def iswinner(self):
        return self.won

os.chdir('advent_2021/4')
with open("input.txt", "r") as f:
    numbers = f.readline().rstrip().split(',')
    numbers = [ int(n) for n in numbers]

    boards = []
    for line in f:
        line = line.rstrip()
        if line:
            boards[-1].addrow(line) 
        else:
            boards.append(Board())

last_n = None
last_winner = None
for n in numbers:
    list(map(lambda b: b.mark(n), boards))
    last_winner = list(filter(lambda b: b.iswinner(), boards))
    if last_winner:
        last_n = n
    boards = list(filter(lambda b: not b.iswinner(), boards))

    if len(boards) == 0:
        break
    
print(last_winner[0].sum() * last_n)