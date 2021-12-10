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
    if len(stack) == 0:
        return 0

def correction(input):
    rubric = {')': 1, ']': 2, '}': 3, '>': 4}
    stack = deque()
    for c in input:
        if c in openers:
            stack.append(c)
        elif c in closers:
            matching_opener = openers[closers.index(c)]
            if len(stack)>0 and stack[-1] == matching_opener:
                stack.pop()

    ret = ""    
    while stack:
        op = stack.pop()   
        cl = closers[openers.index(op)]
        ret += cl 
    #print(len(stack), stack)
    score = 0
    for c in ret:
        score *= 5
        score += rubric[c]
    return score

total_errors = 0

corrected_scores = []
for line in input:
    #line = [ int(n) for n in line ]

    errors=balance_check(line)
    if errors:
        total_errors += errors
    else:
        corrected_scores.append(correction(line))
corrected_scores.sort()

print("part1:", total_errors)

#print(corrected_scores, len(corrected_scores))
print("part2:", corrected_scores[len(corrected_scores)//2])

