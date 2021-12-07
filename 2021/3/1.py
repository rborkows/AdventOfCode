import os

os.chdir('advent_2021/3')

f = open("input.txt", "r")
lines = f.readlines()
f.close()

sum = [0] * (len(lines[0]) - 1)
for line in lines:
    i = 0
    for c in line.rstrip():
        sum[i] += int(c)
        i += 1

n = len(lines)
gamma_list = [ 1 if x > (n/2) else 0 for x in sum ] # good thing the input does not have any ties :-)

e = 1
gamma = 0
epsilon = 0
while len(gamma_list) > 0:
    n = gamma_list.pop()
    m = 0 if n == 1 else 1
    gamma += e * n
    epsilon += e * m
    e *= 2

print(gamma, epsilon, gamma * epsilon)     