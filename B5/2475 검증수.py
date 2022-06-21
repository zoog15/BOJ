s = list(map(int, input().split()))

ans = 0

for i in s:
    ans += i*i

print(ans%10)