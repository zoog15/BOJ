a = int(input())
b = int(input())
c = int(input())
ans = ''

if a == b == c:
    ans = 'Equilateral'
elif a+b+c==180 and a==b or b==c or a==c:
    ans = 'Isosceles'
elif a+b+c==180 and a != b != c:
    ans = 'Scalene'
else:
    ans = 'Error'

print(ans)
