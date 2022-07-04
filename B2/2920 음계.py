nums = list(map(int, input().split()))

l = len(nums)
ans = ""
sum = 0

for i in range(l-1):
    if nums[0] == 1 and nums[i] + 1 == nums[i+1]:
        sum += 1
    elif nums[0] == 8 and nums[i] -1 == nums[i+1]:
        sum += 2

if sum == 7:
    ans = "ascending"
elif sum == 14:
    ans = "descending"
else:
    ans = "mixed"

print(ans)
