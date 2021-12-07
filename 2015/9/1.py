import itertools
from os import pathconf_names

locations = set()
paths = {}
paths_part1 = {}

# correct answer is 117
def part1():
    visited = []
    optimal = []
    
    shortest_path = [ (p, paths_part1[p]) for p in paths_part1 ]
    shortest_path = shortest_path[0][0].split(":")
    shortest_path.sort(key=lambda x: x[1])
    location = shortest_path[0]
    print(f"starting at {location}")
    total_distance = 0
    while len(paths_part1) > 0:
        
        optimal.append(location)
    
        paths_from_here = list(filter(lambda p: location in p, paths_part1.keys()))
        paths_from_here = [ (p, paths_part1[p]) for p in paths_from_here ]
        paths_from_here.sort(key=lambda x: x[1])
        shortest_path = paths_from_here[0][0]
        next_stop = shortest_path.split(":")
        next_stop.remove(location)
        next_stop = next_stop[0]
        total_distance += paths_from_here[0][1]
        path_keys = list(paths_part1.keys())
        for pk in path_keys:
            if location in pk:
                del paths_part1[pk]
        print(location, total_distance)
        location = next_stop

    print(optimal)
    return total_distance

def distance(src, dst) -> int:
    #print(src, dst)
    if f"{src}:{dst}" in paths:
        return paths[f"{src}:{dst}"]
    else:
        return paths[f"{dst}:{src}"]

def measure(itinerary) -> int:
    #print(itinerary)
    total_distance = 0
    location = itinerary[0]
    for next_stop in itinerary[1:]:
        total_distance += distance(location, next_stop)
        location = next_stop
    return total_distance

# Dunno why approach 1 didn't work for longest path, so brute forced it. Only 40k permutations /shrug
def part2():
    print(len(locations))
    distances = []
    for path in itertools.permutations(locations,8):
        distances.append(measure(path))
        #print(path, measure(path))
    return max(distances)

with open("AdventOfCode/2015/9/input.txt", "r") as f:
        for line in f:
            line = line.rstrip()
            a = line.split()
            locations.add(a[0])
            locations.add(a[2])
            paths[f"{a[0]}:{a[2]}"] = int(a[4])
paths_part1 = paths.copy()

print(locations)
#print(f"part1: {part1()}")
print(f"part2: {part2()}")


#path = ['Faerun', 'AlphaCentauri', 'Tambi', 'Snowdin', 'Norrath', 'Tristram', 'Arbre']
#print(measure(path))