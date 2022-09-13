n = int(input())

ans = 0
for i in range(1, n+1):
    if i < 100:
        ans += 1
        continue

    num = str(i)

    if len(num) == 3:
        if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
            ans += 1

print(ans)

