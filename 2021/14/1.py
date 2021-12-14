import sys
sys.path.append("AdventOfCode/lib")
import adventutil
from collections import Counter

fetcher = adventutil.InputFetcher('2021', '14')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def cycle(pairs, rules, elements):
    prev_pairs = pairs.copy()
    for rule in rules:
        elements[rules[rule]] += prev_pairs[rule]
        pairs[rule] -= prev_pairs[rule]
        pairs[rule[0]+rules[rule]] += prev_pairs[rule]
        pairs[rules[rule]+rule[1]] += prev_pairs[rule]    

polymer = input[0]
rules={}
for rule in input[2:]:
    k, _, v = rule.split()
    rules[k] = v

pairs = Counter()
elements = Counter(polymer)
for i in range(len(polymer)-1):
    pair = polymer[i]+polymer[i+1]
    pairs[pair] += 1

for i in range(10):
    cycle(pairs, rules, elements)

freq = elements.most_common()
print("part1:", freq[0][1] - freq[-1][1]) # 2891

for i in range(30):
    cycle(pairs, rules, elements)

freq = elements.most_common()
print("part2:", freq[0][1] - freq[-1][1])  # 4607749009683
