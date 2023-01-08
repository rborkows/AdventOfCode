import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '18')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Cube:
    all_cubes = {}
    def __init__(self, x, y, z, type):
        (self.x, self.y, self.z) = (x, y, z)
        self.all_cubes[(self.x, self.y, self.z)] = self
        self.faces = 0
        self.type = type
        pass

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z, self.type))

    def __str__(self) -> str:
        return f"{self.x}, {self.y}, {self.z} faces:{self.faces} type:{self.type}"

    @classmethod
    def update_faces(cls, acceptable_neighbour=0):
        for key in cls.all_cubes:
            cls.all_cubes[key]._update_faces(acceptable_neighbour)

    def _update_faces(self, acceptable_neighbour):
        self.faces=0
        if self.type == 2: # We only care about solid cubes
            neighbours=self.get_neighbours(acceptable_neighbour)
            for neighbour in neighbours:
                self.faces += 1
    
    def get_neighbours(self, acceptable_neighbour):
        neighbours = []
        if (self.x-1, self.y, self.z) in Cube.all_cubes:
            neighbours.append((self.x-1, self.y, self.z))
        if (self.x+1, self.y, self.z) in Cube.all_cubes:
            neighbours.append((self.x+1, self.y, self.z))
        if (self.x, self.y-1, self.z) in Cube.all_cubes:
            neighbours.append((self.x, self.y-1, self.z))        
        if (self.x, self.y+1, self.z) in Cube.all_cubes:
            neighbours.append((self.x, self.y+1, self.z))
        if (self.x, self.y, self.z-1) in Cube.all_cubes:
            neighbours.append((self.x, self.y, self.z-1))
        if (self.x, self.y, self.z+1) in Cube.all_cubes:
            neighbours.append((self.x, self.y, self.z+1))
        neighbours=list(filter(lambda e: Cube.all_cubes[e].type==acceptable_neighbour, neighbours))
        return neighbours
            
    @classmethod
    def get_exposed_faces(cls):
        exposed_faces=0
        for key in cls.all_cubes:
            if cls.all_cubes[key].type != 2:
                continue
            exposed_faces += cls.all_cubes[key].faces
        return exposed_faces

    @classmethod
    def floodfill(cls, coordinate, type=1):
        if coordinate in cls.all_cubes:
            cls.all_cubes[coordinate]._floodfill(type)

    def _floodfill(self, type):
        if self.type != type:
            #print(f"Flooding {self.x}, {self.y}, {self.z}")
            if type == 1:
                acceptable_neighbour = 0
            else:
                acceptable_neighbour = 1
            self.type = type
            neighbours = self.get_neighbours(acceptable_neighbour)
            for neighbour in neighbours:
                Cube.all_cubes[neighbour]._floodfill(type)

cube_coordinates = []
for line in input:
    coordinate = line.split(',')
    coordinate = [ int(e) for e in coordinate ]
    cube_coordinates.append(coordinate)

min_corner = cube_coordinates[0].copy()
max_corner = cube_coordinates[0].copy()

for coordinate in cube_coordinates:
    for i in range(3):
        min_corner[i] = min(min_corner[i], coordinate[i])
        max_corner[i] = max(max_corner[i], coordinate[i])
min_corner = [ e-1 for e in min_corner ]
max_corner = [ e+1 for e in max_corner ]

part1=0
part2=0

# fill space with type 0 cubes (vacuum)
for x in range(min_corner[0], max_corner[0]+1):
    for y in range(min_corner[1], max_corner[1]+1):
        for z in range(min_corner[2], max_corner[2]+1):
            Cube(x,y,z,0)

# Set input cubes as type 2 (solid)
for coordinate in cube_coordinates:
    Cube.all_cubes[tuple(coordinate)].type = 2

Cube.update_faces(acceptable_neighbour=0)
part1 = Cube.get_exposed_faces()

# floodfill space outside the solid cubes with gas. Should leave vacuum in enclosed areas
sys.setrecursionlimit(10000) # oof
Cube.floodfill(tuple(min_corner), type=1)
Cube.update_faces(acceptable_neighbour=1)
part2 = Cube.get_exposed_faces()

print("part1:", part1) # 4536
print("part2:", part2) # 2606
