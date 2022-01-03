import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '22')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)



class Cuboid:
    def __init__(self, initstring) -> None:
        state, coords = initstring.split()
        if state == "on":
            self.state = 1
        else:
            self.state = 0
        self.ranges = coords.split(",")
        self.ranges = list(map(self._str_to_range, self.ranges))
        
    def _str_to_range(self, str):
        _,rng = str.split("=")
        low, high = rng.split("..")
        return range(int(low), int(high)+1)

    def includes_point(self, x, y, z):
        if x in self.ranges[0] and y in self.ranges[1] and z in self.ranges[2]:
            return self.state
        else:
            return None

    def includes_cuboid(self, c):
        # print(c.ranges, self.ranges)
        x_intersect = set(c.ranges[0]).intersection(set(self.ranges[0]))
        y_intersect = set(c.ranges[1]).intersection(set(self.ranges[1]))
        z_intersect = set(c.ranges[2]).intersection(set(self.ranges[2]))
        
        if len(x_intersect) > 0 and len(y_intersect) > 0 and len(z_intersect) > 0:
            return True
        else:
            return False


class Board:
    def __init__(self) -> None:
        pass

cuboids = []
for line in input:
    cuboids.append(Cuboid(line))

lit = 0
central_cube = Cuboid("on x=-50..50,y=-50..50,z=-50..50")
cuboids = list(filter(lambda c: c.includes_cuboid(central_cube), cuboids))
for x in range(-50,51):
    for y in range(-50,51):
        for z in range(-50,51):
            state = [ c.includes_point(x,y,z) for c in cuboids ]
            state = list(filter(lambda e: e != None, state))
            if state == [] or state[-1] == 0:
                state = 0
            else:
                state = 1
            lit += state         
print("part 1:", lit)




