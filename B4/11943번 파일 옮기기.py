ap1, or1 = map(int, input().split())
ap2, or2 = map(int, input().split())

print(min(ap1+or2, or1+ap2))