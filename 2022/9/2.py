import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '9')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Rope:
    def __init__(self):
        self.head=(0,0)
        self.tail=(0,0)
        self.tail_visited=set([(0,0)])

    def step(self, dir):
        ph = self.head
        if dir=='R':
            self.head = (self.head[0]+1, self.head[1])
        elif dir=='L':
            self.head = (self.head[0]-1, self.head[1])
        elif dir=='U':
            self.head = (self.head[0], self.head[1]+1)
        else:
            self.head = (self.head[0], self.head[1]-1)

        if self.tail != ph:
            if dir=='R':
                if self.tail[0] < ph[0]:
                    self.tail = ph
            elif dir=='L':
                if self.tail[0] > ph[0]:
                    self.tail = ph
            elif dir=='D':
                if self.tail[1] > ph[1]:
                    self.tail = ph
            else:
                if self.tail[1] < ph[1]:
                    self.tail = ph

            self.tail_visited.add(self.tail)
        
    
part1=0
part2=0

r=Rope()

#for s in "RRUU":    
#    r.step(s)


#exit(0)

for line in input:
    a=line.split()
    for n in range(int(a[1])):
        r.step(a[0])
    #print(a,r.tail_visited)

print("part1:", len(r.tail_visited))
print("part2:", part2)
