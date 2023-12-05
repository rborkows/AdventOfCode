import sys
import re


sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2023', '5')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

class Map:
    def __init__(self, dst, src, len) -> None:
        self.dst = range(dst, dst+len)
        self.src = range(src, src+len)

class Mapper:
    def __init__(self, name) -> None:
        self.name = name
        self.maps = []
        self.lowest = None
        self.highest = None
        pass
    
    def parse(self, line):
        a = line.split(' ')
        values = list(map(lambda e: int(e), a))
        self.maps.append(Map(values[0], values[1], values[2]))
        if self.lowest == None or values[1] < self.lowest:
            self.lowest = values[1]
        if self.highest == None or values[1]+values[2]-1 > self.highest:
            self.highest = values[1]+values[2]-1
        
    def map(self, value):
        if value < self.lowest or value > self.highest:
            return(value)
        for map in self.maps:
            if value in map.src:
                offset = value - map.src[0]
                return map.dst[0] + offset
        return(value)


part1=0
seeds = input[0].split(' ')[1:]
seeds = list(map(lambda e: int(e), seeds))
input = input[2:]
mapper_list=[]
for line in input:
    if line.endswith("map:"):
        a=line.split(" ")
        mapper_list.append(Mapper(a[0]))
    elif line == "":
        pass
    else:
        mapper_list[-1].parse(line)

mappers = {}
for mapper in mapper_list:
    mappers[mapper.name] = mapper

locations = []
for seed in seeds:
    soil = mappers["seed-to-soil"].map(seed)
    fertilizer = mappers["soil-to-fertilizer"].map(soil)
    water = mappers["fertilizer-to-water"].map(fertilizer)
    light = mappers["water-to-light"].map(water)
    temperature = mappers["light-to-temperature"].map(light)
    humidity = mappers["temperature-to-humidity"].map(temperature)
    location = mappers["humidity-to-location"].map(humidity)

    locations.append(location)
locations.sort()

print("part1: ", locations[0])

print(sys.argv[1])

# There are 10 different seed ranges. Run 10 different processes, one per range to brute-force it
# gross :-(
lowest = None
i = int(sys.argv[1])
for seed in range(seeds[i], seeds[i]+seeds[i+1]):
    
    soil = mappers["seed-to-soil"].map(seed)
    fertilizer = mappers["soil-to-fertilizer"].map(soil)
    water = mappers["fertilizer-to-water"].map(fertilizer)
    light = mappers["water-to-light"].map(water)
    temperature = mappers["light-to-temperature"].map(light)
    humidity = mappers["temperature-to-humidity"].map(temperature)
    location = mappers["humidity-to-location"].map(humidity)
    if lowest == None or location < lowest:
        lowest = location
        print(lowest)

print("part2: ", lowest)