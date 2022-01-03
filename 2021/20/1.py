import sys
from bitstring import BitArray
from collections import defaultdict
import math

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '20')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

algo = input[0].replace('.', '0')
algo = algo.replace('#', '1')
algo = list(algo)
algo = [ int(e) for e in algo ]
board = defaultdict(int)
row = 0
for line in input[2:]:
    line = line.replace('.', '0')
    line = line.replace('#', '1')
    for col, val in enumerate(line):
        board[(row, col)] = int(val)
    row += 1


def neighbour_string(row, col, board):
    ret = []
    possible_n = [(-1,-1), (-1, 0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]
    for n in possible_n:
        n_row = n[0] + row
        n_col = n[1] + col
        ret.append(board[(n_row, n_col)])
    return ret

# return upper left and lower right corners bounding the points
def extent(board):
    rows = [ e[0] for e in board ]
    rows.sort()
    cols = [ e[1] for e in board ]
    cols.sort()
    return((rows[0], cols[0]), (rows[-1], cols[-1]))

def cycle(board, background = 0):
    if background == 0:
        new_background = algo[0]
    else:
        new_background = algo[511]

    if new_background:
        lit = math.inf
    else:
        lit = 0

    newboard = defaultdict(lambda: new_background)
    ul, lr = extent(board)
    for row in range(ul[0]-1, lr[0]+2):
        for col in range(ul[1]-1, lr[1]+2):
            ns = neighbour_string(row, col, board)
            ba = BitArray(ns)
            lit += algo[ba.uint]
            newboard[(row, col)] = algo[ba.uint]
    return (lit, newboard)

background = 0 # points outside the defined area are zero
for i in range(50): # 2 cycles of full input is 5479
    lit, board = cycle(board, background)
    if lit == math.inf:
        background = 1
    else:
        background = 0
    if i == 1:
        part1 = lit
    elif i==49:
        part2 = lit
    
print("part 1:", part1)
print("part 2:", part2)