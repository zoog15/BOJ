def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        if i == 1:
            answer -= 1
            continue
        elif i == 2:
            answer += 2
            continue
        cnt = 2
        for j in range(2, i):
            if i % j == 0:
                cnt += 1

        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer


print(solution(13,17))
print(solution(24,27))