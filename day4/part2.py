from sys import stdin
from collections import deque

ans = 0

dq = deque([1])

for line in stdin:
    first, second = line.split(":")[1].split("|")
    winning: set[str] = set(first.split())
    have: list[str] = second.split()

    current_instances = dq.popleft() if dq else 1
    ans += current_instances

    count = sum(1 for num in have if num in winning)

    for c in range(count):
        if c < len(dq):
            dq[c] += 1 * current_instances
        else:
            dq.append(1 + current_instances)

print(ans)
