from sys import stdin

seeds = list(map(int, input().split(": ")[1].split(" ")))
input()


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


def transform(seeds: list[int], ruleset: list[list[int]]) -> list[int]:
    new_seeds = []

    for seed in seeds:
        dest_found = False
        for rule in ruleset:
            dest, source, span = rule

            if seed in range(source, source + span):
                new_seeds.append(dest + seed - source)
                dest_found = True
                break

        if not dest_found:
            new_seeds.append(seed)

    return new_seeds


rulesets = get_rulesets()

for rule in rulesets:
    seeds = transform(seeds, rule)

print(min(seeds))
