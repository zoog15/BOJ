n = int(input())
a = list(map(int, input().split()))

a.sort()
new_a = []

for i in a:
    if i not in new_a:
        new_a.append(i)

print(*new_a)