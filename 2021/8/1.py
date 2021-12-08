import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '8')
input = fetcher.fetch(rstrip=True, commasplit=True)

class Display:
    def __init__(self, mappings) -> None:
        self.map = [None] * 10
        unknown_5 = []
        unknown_6 = []
        for mapping in mappings:
            if len(mapping) == 2:
                one = mapping
                self.map[1] = self._to_set(mapping)
            elif len(mapping) == 3:
                seven = mapping
                self.map[7] = self._to_set(mapping)
            elif len(mapping) == 4:
                four = mapping
                self.map[4] = self._to_set(mapping)
            elif len(mapping) == 7:
                eight = mapping
                self.map[8] = self._to_set(mapping)
            elif len(mapping) == 5:
                unknown_5.append(self._to_set(mapping))
            elif len(mapping) == 6:
                unknown_6.append(self._to_set(mapping))
        for n in unknown_5:
            if self.map[1].issubset(n):
                self.map[3] = n 
        unknown_5.remove(self.map[3])
        for n in unknown_6:
            if (one[0] in n and not one[1] in n) or (not one[0] in n and one[1] in n):
                self.map[6] = self._to_set(n)            
        unknown_6.remove(self.map[6])
        self.map[9] = self.map[3].union(self.map[4])
        unknown_6.remove(self.map[9])
        self.map[0] = self._to_set(unknown_6[0])
        seg = self.map[8].difference(self.map[6]).pop()
        if seg in unknown_5[0]:
            self.map[5] = self._to_set(unknown_5[1])
            self.map[2] = self._to_set(unknown_5[0])
        else:
            self.map[5] = self._to_set(unknown_5[0])
            self.map[2] = self._to_set(unknown_5[1])
            
    def _to_set(self, word):
        ret = set()
        for c in word:
            ret.add(c)
        return ret
    
    def decode(self, word):
        word_set = self._to_set(word)
        id = self.map.index(word_set)
        return id

count = 0
sum = 0
for line in input:
    line = line[0]
             
    (left, right) = line.split("|")
    left = left.split()
    right = right.split()
    dp = Display(left)
    decoded = []
    for word in right:
        decoded.append(dp.decode(word))
    
    for n in decoded:
        if n in [1,4,7,8]:
            count += 1
    decoded = [ str(n) for n in decoded ]
    decoded_n = int("".join(decoded))
    sum += decoded_n

print("part1:", count)
print("part2:", sum)