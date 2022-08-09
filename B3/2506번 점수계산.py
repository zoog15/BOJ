n = int(input())

scores = list(map(int, input().split()))

ans = 0
count = 1

for i in scores:
    if i == 1 and count != 0:
        ans += count
        count += 1
    elif i == 0:
        count = 1

print(ans)
