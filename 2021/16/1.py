from re import sub
import sys
from bitstring import BitArray
import math

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2021', '16')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def get_type(b):
    return b[3:6].uint

def get_version(b):
        return b[:3].uint

def is_literal(b):
        return get_type(b)==4

def get_literal(b):
        if not is_literal(b):
            raise ValueError
        p = 6
        keepreading = True
        literal = BitArray()
        while keepreading:  
            keepreading = b[p:p+1]
            chunk = b[p:p+5]
            literal += chunk[1:]
            p += 5
        return (literal.uint, p) # decoded number and last pointer position

def get_subpackets(b):
    lengthtype = b[6:7]  
    # print("lengthtype=", lengthtype)
    if lengthtype:     
        subpacket_count = b[7:18].uint
        # print("subpacket count=", subpacket_count)
    else:
        subpacket_length = b[7:22].uint
        # print("subpacket length=", subpacket_length)
        return b[22:22+subpacket_length]

def split_packets(b):
    # print("b=", b.bin)
    if is_literal(b):
        _, p = get_literal(b)
        return (b[0:p], b[p:])
    lengthtype = b[6:7]
    if lengthtype:
        subpacket_count = b[7:18].uint
        subpacket = b[18:]
        # print("subpacket=", subpacket.bin, subpacket_count)
        for p in range(subpacket_count):
            head, subpacket = split_packets(subpacket)
            # print("v=", get_version(head), get_type(head), subpacket.bin)


        return (head, subpacket)
    else:
        subpacket_length = b[7:22].uint
        return (b[0:22+subpacket_length], b[22+subpacket_length:])


def sum_versions(b):
    # print(f"b = {b[0:3].bin} {b[3:6].bin} {b[6:].bin}")
    sum = get_version(b)
    if is_literal(b):
        # print("literal", sum)
        return sum
    lengthtype = b[6:7]
    if lengthtype:    
        subpacket_count = b[7:18].uint
        # print(f"type 1 with {subpacket_count} subpackets")
        subpacket = b[18:]
        # print("subpacket:", subpacket.bin)
        for p in range(subpacket_count):
            sum += sum_versions(subpacket)
            (head, subpacket) = split_packets(subpacket)
            # print("subpacket version", get_version(head))
    else:
        # print("type 0")
        subpacket_length = b[7:22].uint
        subpacket = b[22:22+subpacket_length]
        while subpacket:
            sum += sum_versions(subpacket)
            (head, subpacket) = split_packets(subpacket)  
            # print(head.bin,subpacket.bin, sum)
    return(sum)

def execute(b):
    # print(f"b = {b[0:3].bin} {b[3:6].bin} {b[6:].bin}")
    if is_literal(b):
        # print("literal", sum)
        return get_literal(b)
    type = get_type(b)
    subpackets = []
    lengthtype = b[6:7]
    if lengthtype:    
        subpacket_count = b[7:18].uint
        # print(f"type 1 with {subpacket_count} subpackets")
        subpacket = b[18:]
        # print("subpacket:", subpacket.bin)
        for p in range(subpacket_count):
            subpackets.append(execute(subpacket))
            (head, subpacket) = split_packets(subpacket)
            # print("subpacket version", get_version(head))
    else:
        # print("type 0")
        subpacket_length = b[7:22].uint
        subpacket = b[22:22+subpacket_length]
        while subpacket:
            subpackets.append((subpacket))
            (head, subpacket) = split_packets(subpacket)  
            # print(head.bin,subpacket.bin, sum)
    ret = 0
    if type == 0:
        subpackets = [ e[0] for e in subpackets ]
        ret = sum(subpackets)
    elif type == 1:
        print("subpackets:", subpackets)
        subpackets = [ e[0] for e in subpackets ]
        ret = math.prod(subpackets)

    return(ret)

b = BitArray("0x" + input[0])
print("part 1:", sum_versions(b)) #873