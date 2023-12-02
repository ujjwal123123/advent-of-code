# part 1

with open("day-1.txt") as f:
    lines = f.readlines()

    nums = []

    for line in lines:
        ans = []
        for char in line:
            if ord("0") <= ord(char) <= ord("9"):
                ans.append(char)
                break
        for char in line[::-1]:
            if ord("0") <= ord(char) <= ord("9"):
                ans.append(char)
                break

        nums.append(int("".join(ans)))

    print(sum(nums))


# part 2
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def check_num(line: str, index: int):
    if "0" <= line[i] <= "9":
        return int(line[i])
    else:
        for num in numbers:
            if i + len(num) <= len(line) and line[i : i + len(num)] == num:
                return numbers[num]

    return None


with open("day-1.txt") as f:
    lines = f.readlines()

    nums = []

    for line in lines:
        ans = []
        for i in range(len(line)):
            ret = check_num(line, i)
            if ret is not None:
                ans.append(str(ret))
                break

        for i in range(len(line) - 1, -1, -1):
            ret = check_num(line, i)
            if ret is not None:
                ans.append(str(ret))
                break

        ans = list(map(str, ans))
        nums.append(int("".join(ans)))

    print(sum(nums))