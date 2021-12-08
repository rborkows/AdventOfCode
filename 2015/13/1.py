import sys
import itertools

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2015', '13')
input = fetcher.fetch(rstrip=True, commasplit=False)

map={}
guests = set()
for line in input:
    (person1, _, direction, magnitude, _, _, _, _, _, _, person2) = line.split()
    person2 = person2[:-1]
    guests.add(person1)
    direction = 1 if direction == "gain" else -1
    map[f"{person1}:{person2}"] = direction * int(magnitude)
    map[f"me:{person1}"] = 0 # comment out for part 1
    map[f"{person1}:me"] = 0 # comment out for part 1
guests.add("me") # comment out for part 1

def score(person1, person2):
    return map[f"{person1}:{person2}"]

max_happiness = -999
for p in itertools.permutations(guests):
    happiness = 0
    for i in range(len(guests)-1):
        happiness += score(p[i], p[i+1])
        happiness += score(p[i+1], p[i])
    happiness += score(p[-1], p[0])
    happiness += score(p[0], p[-1])
    max_happiness = max([happiness, max_happiness])    
print(max_happiness)