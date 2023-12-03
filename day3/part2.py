from sys import stdin

lines: list[str] = []
for line in stdin:
    lines.append(line.strip())

ans: list[int] = []
for l, line in enumerate(lines):

    def check_neighbour(l, c) -> list[int]:
        visited = set()

        def get_num(l: int, c: int) -> int | None:
            line = lines[l]
            num = int(line[c])

            if (l, c) in visited:
                return None

            for i in range(1, c + 1):
                if c - i < 0 or not line[c - i].isnumeric():
                    break
                visited.add((l, c - i))
                num = num + int(line[c - i]) * (10**i)

            for i in range(c + 1, len(line)):
                if not line[i].isnumeric():
                    break
                visited.add((l, i))
                num = num * 10 + int(line[i])

            return num

        nums: list[int] = []
        for dl in (-1, 0, 1):
            if l + dl < 0 or l + dl >= len(lines):
                continue
            for dc in (-1, 0, 1):
                if dl == dc == 0 or c + dc < 0 or c + dc >= len(line):
                    continue
                if lines[l + dl][c + dc].isnumeric():
                    ret = get_num(l + dl, c + dc)
                    if ret is not None:
                        nums.append(ret)

        return nums

    for c, char in enumerate(line):
        if char == "*":
            ret: list[int] = check_neighbour(l, c)
            if len(ret) == 2:
                ans.append(ret[0] * ret[1])


print(sum(ans))
