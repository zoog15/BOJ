import math

n = int(input())

fact_n = math.factorial(n)
cnt = 0

while True:
    if fact_n%10 != 0:
        break
    fact_n //= 10
    cnt += 1

print(cnt)