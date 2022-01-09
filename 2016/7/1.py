import sys
import itertools

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2016', '7')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def containsabba(str):
    for i,c in enumerate(str[:-3]):
        if str[i] == str[i+3] and str[i+1] == str[i+2] and str[i] != str[i+1]:
            return True
    return False

def getaba(str):
    ret = []
    for i,c in enumerate(str[:-2]):
        if str[i] == str[i+2] and str[i] != str[i+1]:
            ret.append("".join(str[i:i+3]))
    return ret

def breakup(str):
    hypernets = []
    addresses = []
    inside = False
    address = ""
    for c in str:
        if c == "[":
            inside = True
            hypernet = ""
            addresses.append(address)
            continue
        elif c == "]":
            inside = False
            hypernets.append(hypernet)
            address = ""
            continue
        if inside:
            hypernet += c
        else:
            address += c
    addresses.append(address)
    return (addresses,hypernets)


def istls(addresses, hypernets):
    hypernets = [ containsabba(e) for e in hypernets ]
    addresses = [ containsabba(e) for e in addresses ]
    if any(hypernets):
        return False
    return any(addresses)

def isssl(addresses, hypernets):
    abas = [ getaba(e) for e in addresses ]
    abas = list(itertools.chain(*abas))
    if len(abas) == 0:
        return False
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        for hypernet in hypernets:
            if bab in hypernet:
                return True
    return False

part1 = 0
part2 = 0
for line in input:
    addresses, hypernets = breakup(line)
    if istls(addresses, hypernets):
        part1 += 1
    if isssl(addresses, hypernets):
        part2 += 1

print("Part1:", part1)
print("Part2:", part2)