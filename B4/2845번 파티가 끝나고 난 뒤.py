p, s = map(int, input().split())
people = p*s

news = list(map(int, input().split()))

for i in news:
    print(i-people, end=' ')