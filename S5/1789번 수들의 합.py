n = int(input())
ans = 0
cnt = 1

while True:
    ans += cnt
    if ans > n:
        break
    cnt += 1

print(cnt-1)