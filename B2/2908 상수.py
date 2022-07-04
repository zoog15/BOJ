a, b = map(str, input().split())

r_a = a[::-1]
r_b = b[::-1]

if r_a > r_b:
    print(r_a)
else:
    print(r_b)