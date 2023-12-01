import sys
import re


sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2023', '1')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

#part1=0
#for line in input:
#    s1 = re.sub(r"^[a-z]*", '', line)
#    s1 = re.sub(r"[a-z]*$", '', s1)
#    cal = int(f"{s1[0]}{s1[-1]}")
#    part1 = part1 + cal
#    print(line, s1, cal)
#print("part1: ", part1)


def first(line):
    patterns = {f"^one": 1, f"^two": 2, f"^three":3, f"^four":4, f"^five":5, f"^six":6, f"^seven":7, f"^eight":8, f"^nine":9}

    while(len(line) > 0):
        for pattern in patterns:
            if re.match(pattern, line):
                return(patterns[pattern])
            elif line[0].isnumeric():
                return(int(line[0]))
        line = line[1:]

    return(0)

def last(line):
    patterns = {f".*one$": 1, f".*two$": 2, f".*three$":3, f".*four$":4, f".*five$":5, f".*six$":6, f".*seven$":7, f".*eight$":8, f".*nine$":9}
    
    while(len(line) > 0):
        for pattern in patterns:
            if re.match(pattern, line):
                return(patterns[pattern])
            elif line[-1].isnumeric():
                return(int(line[-1]))
        line = line[:-1]

    return(0)

part2=0
for line in input:
    
    cal = int(f"{first(line)}{last(line)}")
    print(line, cal)

    part2 += cal
print("part2:", part2)
