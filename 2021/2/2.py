import os
import re

os.chdir('advent_2021/2')
horizontal = 0
depth = 0
aim = 0
with open("input.txt", "r") as f:
    for line in f:
        (operation, value) = line.split()
        value = int(value)
        if operation == "forward":
            horizontal += value
            depth += aim * value
        elif operation == "down":
            aim += value
        elif operation == "up":
            aim -= value
        else:
            print("unexpected operation")

print(horizontal, depth, horizontal * depth)