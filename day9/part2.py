from sys import stdin

ans = []

for line in stdin:
    nums = [int(num) for num in line.split()][::-1]

    new_num = nums[-1]

    while any(num != 0 for num in nums):
        new_nums = []
        for i in range(len(nums) - 1):
            new_nums.append(nums[i + 1] - nums[i])

        new_num += new_nums[-1]
        nums = new_nums

    ans.append(new_num)

print(sum(ans))
