'''
 제일 큰수를 m번만큼 더하고 그 다음수를 남은 횟수만큼만 더하면 끝
'''
# n : 배열 크기, m :숫자가 더해지는 횟수, k : 최대 몇번
n, m, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

bigest = nums[-1]
second = nums[-2]

answer = 0
while True:
    for i in range(k):
        if m == 0:
            break
        answer += bigest
        m -= 1
    if m == 0:
        break
    answer += second
    m -= 1

print(answer)