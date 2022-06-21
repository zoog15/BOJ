a = int(input())
b = int(input())
c = int(input())

num = str(a*b*c)

for i in range(10):
    si = str(i)
    print(num.count(si))

