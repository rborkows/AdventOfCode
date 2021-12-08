import sys

sys.path.append("AdventOfCode/lib")
import adventutil

class Reindeer:
    def __init__(self, string) -> None:
        (self.name, _, _, self.speed, _, _, self.active_duration, _, _, _, _, _, _, self.rest_duration, _) = string.split()
        self.speed = int(self.speed)
        self.active_duration = int(self.active_duration)
        self.rest_duration = int(self.rest_duration)
        self.position = 0
        self.resting = 0
        self.points = 0
        self.active = self.active_duration
        
    def tick(self):
        if self.active:
            self.position += self.speed
            self.active -= 1
            if not self.active:
                self.resting = self.rest_duration
            state = "Active"
        else:
            self.resting -= 1
            if not self.resting:
                self.active = self.active_duration
            state = "Resting"
        #print(f"{self.name} is at position {self.position} and is {state} with {self.points} points")
        return self.position

    def award_point(self, leader_position):
        if self.position == leader_position:
            self.points += 1

        


fetcher = adventutil.InputFetcher('2015', '14')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

reindeers = []
for line in input:
    #line = [ int(n) for n in line ]
    reindeers.append(Reindeer(line))

leader_position = 0
for t in range(2503): #2503
    leader_position = max([ r.tick() for r in reindeers])
    [ r.award_point(leader_position) for r in reindeers]

print("part1:", leader_position) #2695
print("part2:", max([r.points for r in reindeers])) # 1084