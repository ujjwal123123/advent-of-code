from sys import stdin

lines = []
for line in stdin:
    lines.append(line.strip())

nums = []
for l, line in enumerate(lines):
    num = 0
    to_count = False

    def check_ngh(l, c):
        for dl in (-1, 0, 1):
            if l + dl < 0 or l + dl >= len(lines):
                continue
            for dc in (-1, 0, 1):
                if dl == dc == 0 or c + dc < 0 or c + dc >= len(line):
                    continue
                if lines[l + dl][c + dc] == "." or lines[l + dl][c + dc].isnumeric():
                    continue
                return True

        return False

    for c, char in enumerate(line):
        if char.isnumeric():
            num = num * 10 + int(char)
            if not to_count and check_ngh(l, c):
                to_count = True

        else:
            if to_count and num != 0:
                nums.append(num)
            num = 0
            to_count = False

    if to_count and num != 0:
        nums.append(num)


# print(nums)
print(sum(nums))
