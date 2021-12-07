import os
os.chdir('advent_2021/1')
inc = 0
with open("input.txt", "r") as f:
    prev = int(f.readline())
    for line in f:
        cur = int(line)
        if cur > prev:
            inc += 1
        prev = cur
        #print(prev, cur, inc)
print(inc)