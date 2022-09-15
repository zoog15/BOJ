def solution(x, n):
    answer = []
    first = x
    for i in range(n):
        answer.append(x)
        x += first
    return answer


print(solution(-4,2))