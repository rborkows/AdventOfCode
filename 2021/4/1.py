import os

class Board:
    def __init__(self):
        self.board = []
        
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

winner = None
winning_n = None
for n in numbers:
    for board in boards:
        if(board.mark(n)):
            winner = board
            winning_n = n
            break
    if winner:
        break

#winner.display()
print(winner.sum() * winning_n)