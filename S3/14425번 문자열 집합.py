n, m = map(int, input().split())
s = {}

for i in range(n):
    s[i] = input()

cnt = 0
for i in range(m):
    word = input()
    if word in s.values():
        cnt += 1

print(cnt)