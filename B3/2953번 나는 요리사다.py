sums = []
for i in range(5):
    points = list(map(int, input().split()))
    sums.append(sum(points))

print(sums.index(max(sums))+1, max(sums))