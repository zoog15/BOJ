scores = []
# 어떤 문제가 최종점수 포함될지 인덱스 저장
index = []

for i in range(8):
    scores.append(int(input()))

sor_scores = sorted(scores)

sum = 0
for i in range(3, 8):
    sum += sor_scores[i]
    index.append(scores.index(sor_scores[i])+1)

index.sort()

print(sum)
print(*index)

