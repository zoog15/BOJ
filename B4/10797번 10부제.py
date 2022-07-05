n = int(input())
nums = list(map(int, input().split()))

cnt = 0

for i in nums:
    if i == n:
        cnt += 1

print(cnt)