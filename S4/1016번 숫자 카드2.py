answer = {}
n = int(input())

cards = list(map(int, input().split()))
cards.sort()

m = int(input())
nums = list(map(int, input().split()))

for i in cards:
    if i not in answer:
        answer[i] = 1
    else:
        answer[i] += 1

for i in nums:
    result = answer.get(i)
    if result:
        print(answer[i], end=' ')
    else:
        print(0, end=' ')
