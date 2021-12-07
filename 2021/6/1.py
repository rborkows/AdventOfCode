from collections import deque

class Population:
    def __init__(self, initial_timers) -> None:

        fishes = [0] * 9
        self.day = 0
        for timer in initial_timers:
            fishes[timer] += 1
        self.fishes = deque(fishes)

    def simulate(self, days):
        print(f"Initial state: { self.fishes }")
        while self.day < days:
            self.tick()
            print(f"After {self.day: >2} days {sum(self.fishes)}: {self.fishes}")  

    def tick(self):
        self.day += 1
        
        newfish = self.fishes[0]
        self.fishes.rotate(-1)
        self.fishes[6] += newfish

with open("advent_2021/6/input.txt") as f:
    line = f.readline()
    initial_timers = line.rstrip().split(',')
    initial_timers = [ int(n) for n in initial_timers ]

#initial_timers = [3,4,3,1,2]
population = Population(initial_timers)
population.simulate(256)
print(f"At end of simulation population is {population.fishes}, with a sum of {sum(population.fishes)}")