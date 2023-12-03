import sys
from collections import defaultdict

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2023', '3')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class PartNumber:
    def __init__(self, value, locations) -> None:
        self.value = value
        self.locations = locations
    def __str__(self) -> str:
        return(f"{self.value} {self.locations}")
    def neighbour_test(self, coord):
        for char_location in self.locations:
            if coord == (char_location[0]-1, char_location[1]):
                return True
            if coord == (char_location[0]+1, char_location[1]):
                return True
            if coord == (char_location[0]-1, char_location[1]-1):
                return True
            if coord == (char_location[0]+1, char_location[1]-1):
                return True
            if coord == (char_location[0]-1, char_location[1]+1):
                return True
            if coord == (char_location[0]+1, char_location[1]+1):
                return True
            if coord == (char_location[0], char_location[1]-1):
                return True
            if coord == (char_location[0], char_location[1]+1):
                return True
        return False

part1=0
symbols=['-', '@', '&', '#', '*', '%', '$', '/', '=', '+']
dim = len(input)


gears = defaultdict(list)
parts = []
symbol_addresses = []
mult_addresses = []
for row in range(dim):
    curnum = []
    addresses = []
    for col in range(dim):
        if input[row][col] in symbols:
            symbol_addresses.append((row, col))
        if input[row][col] == "*":
            mult_addresses.append((row, col))
        if input[row][col].isnumeric():
            curnum.append(input[row][col])
            addresses.append((row, col))
        elif len(curnum)>0 and (input[row][col] == "." or input[row][col] in symbols):
            curnum = int("".join(curnum))
            parts.append(PartNumber(curnum, addresses))
            curnum = []
            addresses = []
    if len(curnum)>0:
        curnum = int("".join(curnum))
        parts.append(PartNumber(curnum, addresses))
        curnum = []
        addresses = []
    curnum = []
    addresses = []

part1 = 0
for part in parts:
    for symbol_address in symbol_addresses:
        if part.neighbour_test(symbol_address):
            part1 += part.value
print("part1:", part1)

part2 = 0
gears = defaultdict(list)
for mult_address in mult_addresses:
    for part in parts:
        if part.neighbour_test(mult_address):
            gears[mult_address].append(part)

for mult_address in gears:
    if len(gears[mult_address]) == 2:
        part2 += gears[mult_address][0].value * gears[mult_address][1].value
print("part2:", part2)




        
           


        


