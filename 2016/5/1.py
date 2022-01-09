import sys
import hashlib

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2016', '5')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

n = 0
part1 = ""
part2 = [None] * 8
prefix = "abc"
prefix = input[0]
while not all(part2):
    doorid = prefix + str(n)
    hash = hashlib.md5(doorid.encode('utf-8')).hexdigest()
    if hash.startswith("00000"):
        part1 = part1 + hash[5]
        if hash[5].isnumeric() and int(hash[5]) < 8 and part2[int(hash[5])] == None:
            part2[int(hash[5])] = hash[6]
        print(part1, part2)
    n += 1

print("Part1:", part1[:8])
print("Part2:", "".join(part2))