n, k = map(int, input().split())

score = list(map(int, input().split()))

score.sort()

for i in range(k-1):
    score.pop()

print(max(score))
