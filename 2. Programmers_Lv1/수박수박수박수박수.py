def solution(n):
    answer = ''
    mok = n // 2
    namu = n % 2

    answer += "수박" * mok
    if namu == 1:
        answer += "수"
    return answer


print(solution(3))