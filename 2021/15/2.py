import sys

sys.path.append("AdventOfCode/lib")
import adventutil
from board import Board
from collections import defaultdict, deque
import math

class Board_NoDiag(Board):
    def neighbours(self, row, col):
        ret = []
        possible_n = [[0, -1],
        [-1,0], [1,0],
        [0,1]]
        for n in possible_n:
            n_row = n[0] + row
            n_col = n[1] + col
            if n_row >=0 and n_row <len(self.board) and n_col >= 0 and n_col <len(self.board[0]):
                ret.append([n_row, n_col])
        return ret

    def value(self, point):
        return self.board[point[0]][point[1]]
    
    def set(self, point, value):
        self.board[point[0]][point[1]] = value

fetcher = adventutil.InputFetcher('2021', '15')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def safest_path(risk):
    t = []
    for row in range(len(risk)):
            t.append([math.inf] * len(risk[0]))
    t[0][0] = 0
    lrp=Board_NoDiag(t)
    risk = Board_NoDiag(risk)
    border = deque()
    border.append([0,0])
    while border:
        point = border.popleft()
        for n in lrp.neighbours(point[0], point[1]):
            
            current_neighbour_lrp = lrp.value(n)
            risk_from_here_to_neighbour = lrp.value(point) + risk.value(n)
            if  current_neighbour_lrp > risk_from_here_to_neighbour:
                lrp.set(n, risk_from_here_to_neighbour)
                border.append(n)
    return lrp.value((lrp.rows-1, lrp.columns-1))
            
def expand(input):
    cave = []
    for line in input:
        line = [ int(n) for n in line ]
        multiline = []
        for i in range(5):
            nl = line.copy()
            nl = [ ((n+i-1) % 9)+1 for n in nl ]
            multiline.append(nl)

        multiline = [item for sublist in multiline for item in sublist]
        cave.append(multiline)
    l = len(cave)
    for i in range(1,5):
        for j in range(l):
            nl = cave[j].copy()
            nl = [ ((n+i-1) % 9)+1 for n in nl ]
            cave.append(nl)
    return cave

cave = []
for line in input:
    line = [ int(n) for n in line ]
    cave.append(line)



#print("part1:", safest_path(cave))
cave = expand(input)
print("part2:", safest_path(cave)) # 2916