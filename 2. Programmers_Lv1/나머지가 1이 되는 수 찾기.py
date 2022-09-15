def solution(n):
    i = 2
    while True:
        if n % i == 1:
            answer = i
            break
        i += 1
    return answer


print(solution(10))