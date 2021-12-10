import sys
from collections import deque

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '10')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

openers = ['(', '{', '[', '<']
closers = [')', '}', ']', '>']

def balance_check(input):
    rubric = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = deque()
    for c in input:
        if c in openers:
            stack.append(c)
        elif c in closers:
            matching_opener = openers[closers.index(c)]
            if len(stack)>0 and stack[-1] == matching_opener:
                stack.pop()
            else:
                return rubric[c]
    return stack

def correction(corrupted_stack):
    rubric = {')': 1, ']': 2, '}': 3, '>': 4}
    ret = ""
    while corrupted_stack:
        op = corrupted_stack.pop()   
        cl = closers[openers.index(op)]
        ret += cl

    score = 0
    for c in ret:
        score *= 5
        score += rubric[c]
    return score

total_errors = 0
corrected_scores = []
for line in input:
    bc = balance_check(line)
    if type(bc) == int:
        total_errors += bc
    else:
        corrected_scores.append(correction(bc))
corrected_scores.sort()

print("part1:", total_errors) # 278475
print("part2:", corrected_scores[len(corrected_scores)//2]) # 3015539998