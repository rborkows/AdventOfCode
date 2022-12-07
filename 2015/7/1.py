import sys
from time import sleep

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2015', '7')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)
part1=0
part2=0


nodes=[]
wires = {}
for line in input:
    nodes.append(line.split())

orig_nodes = nodes.copy()

while len(nodes) > 0:
    unresolved = []
    for node in nodes:
        if(len(node)) == 3: # Assignment
            if node[0].isnumeric():
                wires[node[2]] = int(node[0])
            elif node[0] in wires:
                wires[node[2]] = wires[node[0]]
            else:
                unresolved.append(node)
        elif(len(node) == 4): # NOT
            if node[1] in wires:
                wires[node[3]] = wires[node[1]]^65535
            else:
                unresolved.append(node)
        elif node[1] == 'AND':
            if node[0] in wires and node[2] in wires:
                wires[node[4]] = wires[node[0]] & wires[node[2]]
            elif node[0].isnumeric() and node[2] in wires:
                wires[node[4]] = int(node[0]) & wires[node[2]]
            else:
                unresolved.append(node)
        elif node[1] == 'OR':
            if node[0] in wires and node[2] in wires:
                wires[node[4]] = wires[node[0]] | wires[node[2]]
            else:
                unresolved.append(node)
        elif node[1] == 'LSHIFT':
            if node[0] in wires:
                wires[node[4]] = wires[node[0]] << int(node[2])
            else:
                unresolved.append(node)
        elif node[1] == 'RSHIFT':
            if node[0] in wires:
                wires[node[4]] = wires[node[0]] >> int(node[2])
            else:
                unresolved.append(node)      
        else:
            print("UNKNOWN", node)
    nodes=unresolved
    

print("part1:", wires['a'])

a=wires['a']
wires={'b': a}
nodes=orig_nodes
while len(nodes) > 0:
    unresolved = []
    for node in nodes:
        if(len(node)) == 3: # Assignment
            if node[0].isnumeric() and node[2] not in wires:
                wires[node[2]] = int(node[0])
            elif node[0] in wires:
                wires[node[2]] = wires[node[0]]
            elif node[2] in wires:
                pass
            else:
                unresolved.append(node)
        elif(len(node) == 4): # NOT
            if node[1] in wires:
                wires[node[3]] = wires[node[1]]^65535
            else:
                unresolved.append(node)
        elif node[1] == 'AND':
            if node[0] in wires and node[2] in wires:
                wires[node[4]] = wires[node[0]] & wires[node[2]]
            elif node[0].isnumeric() and node[2] in wires:
                wires[node[4]] = int(node[0]) & wires[node[2]]
            else:
                unresolved.append(node)
        elif node[1] == 'OR':
            if node[0] in wires and node[2] in wires:
                wires[node[4]] = wires[node[0]] | wires[node[2]]
            else:
                unresolved.append(node)
        elif node[1] == 'LSHIFT':
            if node[0] in wires:
                wires[node[4]] = wires[node[0]] << int(node[2])
            else:
                unresolved.append(node)
        elif node[1] == 'RSHIFT':
            if node[0] in wires:
                wires[node[4]] = wires[node[0]] >> int(node[2])
            else:
                unresolved.append(node)      
        else:
            print("UNKNOWN", node)
    nodes=unresolved

print("part2:", wires['a'])
