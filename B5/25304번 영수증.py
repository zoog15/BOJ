money = int(input())
stack = int(input())

total = 0
for i in range(stack):
    a, b = map(int, input().split())
    total += a * b

if money == total:
    print("Yes")
else:
    print("No")