from sys import stdin

turns = input()
input()

mapping = dict()


for line in stdin:
    key, val = line.split(" = ")
    mapping[key] = val.strip("()\n").split(", ")

curr_pos = "AAA"
i = 0

while curr_pos != "ZZZ":
    direction = turns[i % len(turns)]

    if direction == "R":
        curr_pos = mapping[curr_pos][1]
    elif direction == "L":
        curr_pos = mapping[curr_pos][0]
    i += 1

print(i)
