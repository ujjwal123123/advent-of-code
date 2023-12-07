from sys import stdin
from collections import Counter

pairs = []


def comparator(hand):
    ans = []

    c = sorted(list(Counter(hand).values()), reverse=True)

    if c[0] == 5:
        ans.append(0)
    elif c[0] == 4:  # four of a kind:
        ans.append(1)
    elif c[0] == 3 and c[1] == 2:  # full house:
        ans.append(2)
    elif c[0] == 3 and c[1] == c[2] == 1:  # three of a kind:
        ans.append(3)
    elif c[0] == c[1] == 2:  # two pair:
        ans.append(4)
    elif c[0] == 2 and c[1] == c[2] == c[3]:  # pair:
        ans.append(5)
    else:
        ans.append(6)

    strength = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")

    for char in hand:
        ans.append(strength.index(char))

    return ans


for line in stdin:
    hand = line.split()[0]
    bid = int(line.split()[1])
    pairs.append((hand, bid))


pairs.sort(key=lambda x: comparator(x[0]), reverse=True)

ans = 0
for i, (_, bid) in enumerate(pairs):
    ans += bid * (i + 1)

print(ans)
