import sys
from time import time

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '21')
input = fetcher.fetch(rstrip=True, commasplit=False, small=True)

class Dice:
    def __init__(self) -> None:
        self.rolls = 0
    
    def roll(self):
        self.rolls += 1
        return ((self.rolls - 1) % 100) + 1

class Player:
    def __init__(self, id, position) -> None:
        self.position = position
        self.id = id
        self.score = 0

    def play(self, die):
        roll = 0
        for i in range(3):
            roll += die.roll()
        self.advance(roll)

    def advance(self, count):
        self.position += count
        self.position = ((self.position - 1) % 10) + 1 
        self.score += self.position
        

players = []
for line in input:
    a = line.split()
    players.append(Player(int(a[1]), int(a[4])))
d = Dice()

t0 = time()
turn = 0
scores = []
while True:
    player = players[turn%len(players)]
    turn += 1
    player.play(d)
    scores = [ player.score for player in players ]
    if max(scores) >= 1000:
        break

print("part 1:", d.rolls * min(scores)) # 739785