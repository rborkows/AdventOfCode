import sys
import re
from collections import defaultdict


sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2023', '4')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Card:
    def __init__(self, line) -> None:
        #m = re.match(r"^Card\s+(\d+)", line)
        self.copies = 1
        line = re.sub(" +", " ", line)
        a = line.split(' ')
        self.id = int(a[1][:-1])
        a=a[2:]
        self.haves = []
        self.winners = []
        self._score = None
        while a[0].isnumeric():
            self.winners.append(int(a.pop(0)))
        a.pop(0)
        while len(a) > 0:
            self.haves.append(int(a.pop(0)))
  
    def winner_count(self):
        winners = 0
        for have in self.haves:
            if have in self.winners:
                winners += 1
        return(winners)

    def score(self):
        if self._score != None:
            return self._score
        
        winners = self.winner_count()
        if winners == 0:
            self._score = 0
        else:
            self._score = 2**(winners-1)
        return self._score
    
    def addcopy(self):
        self.copies += 1
        

cards = []
for line in input:
    cards.append(Card(line))

part1 = 0
for card in cards:
    part1 += card.score()
print("part1:", part1)

part2 = 0
for id, card in enumerate(cards):
    for copy in range(card.copies):
        for i in range(id+1, id+1+card.winner_count()):
            cards[i].addcopy()

for id, card in enumerate(cards):
    part2 += card.copies
print("part2:", part2)
