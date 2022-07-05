money, get, have = map(int, input().split())

ans = money*get-have

if ans < 0:
    ans = 0

print(ans)