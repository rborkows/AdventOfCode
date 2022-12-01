import sys
import math

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2019', '2')
input = fetcher.fetch(rstrip=True, commasplit=True, small=False)
input = input[0]
input = [ int(e) for e in input ]



def intcode(code):
    ip = 0
    while code[ip] != 99:
        if code[ip] == 1: # add
            code[code[ip+3]] = code[code[ip+1]] + code[code[ip+2]]
            ip += 4
        elif code[ip] == 2: # multiply
            code[code[ip+3]] = code[code[ip+1]] * code[code[ip+2]]
            ip += 4
        else:
            print("wtf")
            exit(1)


memory = input.copy()
memory[1] = 12
memory[2] = 2
intcode(memory)
print("part1:", memory[0])
for noun in range(1,100):
    for verb in range(1,100):
        memory = input.copy()
        memory[1]=noun
        memory[2] = verb
        intcode(memory)
        if memory[0] == 19690720:
            print("part2:", 100 * noun + verb)
            break