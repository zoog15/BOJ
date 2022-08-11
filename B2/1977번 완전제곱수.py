m = int(input())
n = int(input())

nums = []
a = 1

while True:
    if pow(a,2) > n:
        break
    if pow(a,2) >= m and pow(a,2) <= n:
        nums.append(pow(a,2))
    a += 1

if len(nums) != 0:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)
