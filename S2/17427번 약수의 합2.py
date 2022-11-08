def solution(n):
    answer = 0

    for i in range(1, n+1):
        answer += (n//i) * i

    return answer


n = int(input())

print(solution(n))
