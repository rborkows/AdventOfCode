import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '11')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class School:
    def __init__(self,input) -> None:
        self.board = []
        self.flashes = 0
        for line in input:
            newline = []
            for c in line:
                newline.append(int(c))
            self.board.append(newline)

    def display(self):
        for row in self.board:
            print(row)

    def get_flashers(self):
        ret = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] > 9:
                    ret.append([row,col])
        return ret

    def neighbours(self, row, col):
        ret = []
        possible_n = [[-1,-1], [0, -1], [1,-1],
        [-1,0], [1,0],
        [-1,1], [0,1], [1,1]]
        for n in possible_n:
            n_row = n[0] + row
            n_col = n[1] + col
            if n_row >=0 and n_row <len(self.board) and n_col >= 0 and n_col <len(self.board[0]):
                ret.append([n_row, n_col])
        return ret

    def tick(self):
        for row in range(len(self.board)):
            for  col in range(len(self.board[0])):
                self.board[row][col] += 1
        all_flashers = []
        while True:
            flashers = self.get_flashers()
            all_flashers += flashers
            if flashers == []:
                break
            for flasher in flashers:
                self.flashes += 1
                
                for n in self.neighbours(flasher[0], flasher[1]):
                    self.board[n[0]][n[1]] += 1    
                self.board[flasher[0]][flasher[1]] = 0  
        for flasher in all_flashers:
            self.board[flasher[0]][flasher[1]] = 0
            
        return len(all_flashers)

sc = School(input)

brightstep = 0
part1 = 0
for step in range(2000):
    n_flashers = sc.tick()
    if step == 99:
        part1 = sc.flashes

    if n_flashers == 100:
        brightstep = step + 1
        break

print("part1", part1) # 1625
print("part2", brightstep) # 244