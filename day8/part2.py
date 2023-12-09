from sys import stdin
from math import lcm

turns = input()
input()

mapping = dict()


for line in stdin:
    key, val = line.split(" = ")
    mapping[key] = val.strip("()\n").split(", ")

positions = [pos for pos in mapping.keys() if pos[-1] == "A"]


def get_step_count(position):
    i = 0
    while not position.endswith("Z"):
        direction = turns[i % len(turns)]

        if direction == "R":
            position = mapping[position][1]
        elif direction == "L":
            position = mapping[position][0]
        i += 1

    return i


step_counts = [get_step_count(pos) for pos in positions]
print(lcm(*step_counts))
