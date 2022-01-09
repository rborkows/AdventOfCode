import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2016', '2')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Board:
    def __init__(self, complex = False, position = "5") -> None:
        if complex:
            self.board={"1": {"D":"3"},
                "2": {"R":"3", "D":"6"},
                "3": {"L":"2", "R":"4", "U":"1", "D":"7"},
                "4": {"L":"3", "D":"8"},
                "5": {"R":"6"},
                "6": {"L":"5", "U":"2", "R":"7", "D":"A"},
                "7": {"L":"6", "U":"3", "R":"8", "D":"B"},
                "8": {"L":"7", "U":"4", "R":"9", "D":"C"},
                "9": {"L":"8"},
                "A": {"U":"6", "R":"B"},
                "B": {"L":"A", "U":"7", "R":"C", "D":"D"},
                "C": {"L":"B", "U":"8"},
                "D": {"U":"B"}
            }
        else:
            self.board={"1": {"R":"2", "D":"4"},
                "2": {"L":"1", "R":"3", "D":"5"},
                "3": {"L":"2", "D":"6"},
                "4": {"U":"1", "R":"5", "D":"7"},
                "5": {"L":"4", "U":"2", "R":"6", "D":"8"},
                "6": {"L":"5", "U":"3", "D":"9"},
                "7": {"U":"4", "R":"8"},
                "8": {"L":"7", "U":"5", "R":"9"},
                "9": {"L":"8", "U":"6"}
            }
        self.position = position

    def move(self, instructions):
        for c in instructions:
            if c in self.board[self.position]:
                self.position = self.board[self.position][c]
        return self.position

b = Board()
c = Board(complex=True)
part1 = ""
part2 = ""
for line in input:
    line = line.rstrip()
    
    n = b.move(line)
    part1 += n
    
    n = c.move(line)
    part2 += n
    
print("Part1:", part1)
print("Part2:", part2)