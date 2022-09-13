# n : 동전 종류, k : 목표 금액
n, k = map(int, input().split())

coins = []
cnt = 0

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

for i in coins:
    mok = k // i
    cnt += mok
    k -= mok * i

    if k == 0:
        break

print(cnt)


