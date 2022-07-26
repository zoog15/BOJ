odd = []
odd_sum = 0

for i in range(7):
    n = int(input())
    if n % 2 == 1:
        odd_sum += n
        odd.append(n)

if len(odd) == 0:
    print("-1")
else:
    print(odd_sum)
    print(min(odd))