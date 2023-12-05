from pprint import pprint
from sys import stdin


def get_seeds():
    seeds = list(map(int, input().split(": ")[1].split(" ")))

    new_seeds = []
    for i in range(0, len(seeds), 2):
        new_seeds.append((seeds[i], seeds[i + 1] + seeds[i] - 1))

    return new_seeds


def get_rulesets() -> list[list[list[int]]]:
    rulesets = []

    ruleset = []
    for line in stdin:
        if line == "\n":
            rulesets.append(ruleset)
            ruleset = []
        elif line[0].isalpha():
            continue
        else:
            ruleset.append(list(map(int, line.split())))

    if ruleset:
        rulesets.append(ruleset)
        ruleset = []

    return rulesets


def transform(seed: tuple[int, int], ruleset: list[list[int]]) -> list[tuple[int, int]]:
    # with help from https://www.youtube.com/watch?v=NmxHw_bHhGM
    new_seeds = []

    for rule in ruleset:
        dest, source, span = rule
        seed_start, seed_end = seed

        overlap_start = max(seed_start, source)
        overlap_end = min(seed_end, source + span - 1)

        if overlap_start < overlap_end:
            diff = dest - source
            new_seeds.append((overlap_start + diff, overlap_end + diff))

    return new_seeds or [seed]


if __name__ == "__main__":
    seeds: list[tuple[int, int]] = get_seeds()
    print("original", seeds)
    input()
    rulesets = get_rulesets()

    for ruleset in rulesets:
        new_seeds = []
        for seed in seeds:
            new_seeds += transform(seed, ruleset)
        seeds = new_seeds

    print(min(min(seeds)))
