from sys import stdin

ans = 0

for line in stdin:
    first, second = line.split(":")[1].split("|")
    winning: set[str] = set(first.split())
    have: list[str] = second.split()

    count = 0
    for num in have:
        if num in winning:
            count += 1

    ans += (1 << count) // 2

print(ans)
