import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dogam = {}

for i in range(1, n+1):
    s = input().rstrip()
    dogam[i] = s
    dogam[s] = i

for i in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(dogam[int(a)])
    else:
        print(dogam[a])
