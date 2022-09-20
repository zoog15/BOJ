import math


def sosu(n):
    nums = [True] * (n+1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i]:
            j = 2
            while i * j <= n:
                nums[i*j] = False
                j += 1

    return nums


n, m = map(int, input().split())

sosus = sosu(m)

for i in range(n, m+1):
    if i == 1:
        continue
    if sosus[i]:
        print(i)

