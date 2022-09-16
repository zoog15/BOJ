def solution(s):
    answer = ''
    l_s = list(s)
    l_s.sort(reverse=True)

    for i in l_s:
        answer += i
    return answer


print(solution("Zbcdefg"))