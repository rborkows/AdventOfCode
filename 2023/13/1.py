import sys
import numpy as np

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2023', '13')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Puzzle:
    def __init__(self, puzzle):
        self.puzzle = np.array(puzzle)
        self.original_split = None
        self.orientation = "H"

    def find_split(self):
        row_hashes = [ hash(row.tobytes()) for row in self.puzzle]
        for split in range(1,len(row_hashes)):
            is_mirror = True
            a = row_hashes[:split]
            a.reverse()
            b = row_hashes[split:]

            for i in range(min(len(a), len(b))):
                if a[i] != b[i]:
                    is_mirror = False
                    break
            if is_mirror and self.original_split != f"{self.orientation}:{split}":
                return split
        return False
    
    def transpose(self):
        self.puzzle = self.puzzle.transpose()
        if self.orientation == "H":
            self.orientation = "V"
        else:
            self.orientation = "H"

    def score(self):
        score = 0
        split = self.find_split()
        if split:
            if not self.original_split:
                self.original_split = f"H:{split}"
                score += 100*split
            else:
                score += 100*split
        self.transpose()
        #self.pprint()
        split = self.find_split()
        if split:
            if not self.original_split:
                self.original_split = f"V:{split}"
                score += split
            else:
                score += split
        self.transpose()
        return score
    
    def pprint(self):
        for row in self.puzzle:
            row_t = [ '.' if e==-1 else '#' for e in row]
            print("".join(row_t))
    
    def desmudge(self):
        for r in range(self.puzzle.shape[0]):
            for c in range(self.puzzle.shape[1]):
                self.puzzle[r][c] *= -1
                score = self.score()
                if score:
                    return score
                self.puzzle[r][c] *= -1

puzzles = []
puzzle = []
for line in input:
    if line:
        converted_line = [ -1 if x=='.' else 1 for x in line ]
        puzzle.append(converted_line)
    else:
        puzzles.append(puzzle)
        puzzle = []
puzzles.append(puzzle)

part1 = 0
part2 = 0
for puzzle in puzzles:
    p = Puzzle(puzzle)
    part1 += p.score()
    part2 += p.desmudge()

print("part1:", part1)
print("part2:", part2)