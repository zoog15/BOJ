nums = []

for i in range(10):
    n = int(input())
    nums.append(n%42)

set_nums = set(nums)

print(len(set_nums))