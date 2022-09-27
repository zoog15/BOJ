n, m = map(int, input().split())

listen = set()
look = set()


for i in range(n):
    listen.add(input())

for i in range(m):
    look.add(input())

answer = sorted(set(listen & look))

print(len(answer))
for i in answer:
    print(i)