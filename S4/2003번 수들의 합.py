n, m = map(int, input().split())
cnt = 0

array = list(map(int, input().split()))

start, end = 0, 1
while n >= end >= start:

    sums = array[start:end]
    total = sum(sums)

    if total == m:
        cnt += 1
        end += 1
    elif total < m:
        end += 1
    else:
        start += 1

print(cnt)


