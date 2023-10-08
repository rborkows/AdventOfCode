total_paper = 0
total_ribbon = 0

def box2paper(box):
    paper = 2*box[0]*box[1] + 2*box[1]*box[2] + 2*box[0]*box[2] + box[0]*box[1]
    return(paper)

def box2ribbon(box):
    ribbon = box[0] * box[1] * box[2] + 2*box[0] + 2*box[1]
    return(ribbon)

with open("aoc/2015/2/input","r") as f:
    for box_string in f:
        box_string = box_string.rstrip()
        box = box_string.split("x")
        box = [int(box[0]), int(box[1]), int(box[2])]
        box.sort()

        total_paper += box2paper(box)
        total_ribbon += box2ribbon(box)
    

print("part1=", total_paper)
print("part2=", total_ribbon)