n = int(input())
times = list(map(int, input().split()))

ans = 0

times.sort()

for i in range(n):
    ans += times[i] * (n-i)

print(ans)