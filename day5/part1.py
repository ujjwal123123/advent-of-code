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


def transform(seed: int, ruleset: list[list[int]]) -> int:
    for rule in ruleset:
        dest, source, span = rule

        if seed in range(source, source + span):
            return dest + seed - source

    return seed


rulesets = get_rulesets()

for ruleset in rulesets:
    seeds = [transform(seed, ruleset) for seed in seeds]

print(min(seeds))
