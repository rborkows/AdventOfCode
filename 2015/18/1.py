import sys


sys.path.append("AdventOfCode/lib")
import adventutil
import board

fetcher = adventutil.InputFetcher('2015', '18')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class LightBoard(board.Board):
    def __init__(self, board) -> None:
        super().__init__(board)
        self.corners = [[0,0], [self.rows-1, 0], [self.rows-1, self.columns-1], [0, self.columns-1]]

    def tick(self, skipcorners = False):
        turn_on = []
        turn_off = []
        for row in range(self.rows):
            for col in range(self.columns):
                lit_neighbours = sum([ self.board[r][c] for r,c in self.neighbours(row,col) ])
                if self.board[row][col]:      
                    if lit_neighbours not in [2,3]:
                        turn_off.append([row, col])
                else:
                    if lit_neighbours == 3:
                        turn_on.append([row, col])
        for light in turn_on:
            self.board[light[0]][light[1]] = True
        for light in turn_off:
            if skipcorners:
                if light in self.corners:
                    continue
            self.board[light[0]][light[1]] = False

    def litcount(self):
        ret = 0
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col]:
                    ret += 1
        return ret

b = []
b2 = []
for line in input:
    row = [ c == '#' for c in line ]
    b.append(row)
    b2.append(row.copy())

board = LightBoard(b)
board2 = LightBoard(b2)
board2.board[0][0] = True
board2.board[board2.rows-1][0] = True
board2.board[board2.rows-1][board2.columns-1] = True
board2.board[0][board2.columns-1] = True

for step in range(100):
    board.tick(skipcorners = False)
    board2.tick(skipcorners = True)

print("part1:", board.litcount()) # 1061
print("part2:", board2.litcount())