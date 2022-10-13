s = list(input())

s.sort(reverse=True)
sums = 0
for i in s:
    sums += int(i)

if sums % 3 != 0 or '0' not in s:
    print(-1)
else:
    print("".join(s))