n = int(input())
ans = 0

for i in range(n):
    student, apple = map(int, input().split())
    ans += apple%student

print(ans)