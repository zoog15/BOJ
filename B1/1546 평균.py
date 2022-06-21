# 시험본 과목수
n = int(input())

score = list(map(int, input().split()))

# 최대점수
max_score = max(score)

new_score = []

for i in score:
    change = i/max_score*100
    new_score.append(change)

print(sum(new_score)/n)