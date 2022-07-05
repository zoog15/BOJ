a, b, c = map(int, input().split())

# 몇 개가 같은지 확인
cnt = 1

money = 0
dice = 0
if a == b != c:
    dice = a
    cnt = 2
elif a != b == c:
    dice = b
    cnt = 2
elif a == c != b:
    dice = c
    cnt = 2
elif a == b == c:
    dice = a
    cnt = 3

if cnt == 1:
    money = max(a,b,c)*100
elif cnt == 2:
    money = 1000 + (dice*100)
elif cnt == 3:
    money = 10000 + (dice*1000)

print(money)