import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '17')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def solver_x(success_range):
    ret = []
    for v_init in range(0, success_range[-1]+1):
        p = 0
        for step in range(1,1000):
            if step <= v_init:
                p = v_init * step - ((step * (step - 1)) / 2)
            if p in success_range:
                ret.append((step,v_init))
            
    return ret

def solver_y(success_range):
    ret = []
    for v_init in range(success_range[0],1000):
        max_p = 0
        for step in range(1,1000):
            p = v_init * step - ((step * (step - 1)) / 2)
            if p > max_p:
                max_p = p
            if p in success_range:
                ret.append((step,v_init, max_p))
            if p < success_range[0]:
                break
    
    return ret
def str2range(str):
    a=str[2:].split("..")
    a[1] = a[1].replace(",", "")
    return range(int(a[0]), int(a[1])+1) 

a=input[0].split()
range_x = str2range(a[2])
range_y = str2range(a[3])

x_solutions = solver_x(range_x)
y_solutions = solver_y(range_y)

solutions = set()
for x_solution in x_solutions:
    step = x_solution[0]
    init_x = x_solution[1]
    for match in filter(lambda e: e[0] == step, y_solutions):
        solutions.add((init_x, match[1], match[2]))
solutions = list(solutions)
solutions.sort(key=lambda e: e[2], reverse=True)

print("part1:", int(solutions[0][2]))
print("part2:", len(solutions))