n = int(input())
nums = list(map(int, input().split()))

# 소수 갯수를 셀 카운트
cnt = 0

for i in nums:
    yaksu = 0
    for j in range(1, i+1):
        if i%j == 0:
            yaksu += 1
    if yaksu == 2:
        cnt += 1

print(cnt)
