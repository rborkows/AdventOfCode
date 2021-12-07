import os
os.chdir('advent_2021/1')
inc = 0
a = []
with open("input.txt", "r") as f:
    for line in f:
        a.append(int(line))
    
p = 0
#print(len(a), p+4, 10 < 4)
while len(a) >= (p + 4):
    n1 = a[p] + a[p+1] + a[p+2]
    n2 = a[p+1] + a[p+2] + a[p+3]
    #print(p, n1, n2, inc)
    if n2 > n1:
        inc += 1
    p += 1
print(inc)
