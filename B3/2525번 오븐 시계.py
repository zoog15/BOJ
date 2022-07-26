m, s = map(int, input().split())

t = int(input())

s += t

while True:
    if s >= 60:
        s -= 60
        m += 1
    else:
        break

if m >= 24:
    m -= 24

print(m,s)
