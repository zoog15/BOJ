def solution(n):
    str_n = list(str(n))
    str_n.sort(reverse=True)

    answer = "".join(str_n)

    return int(answer)


print(solution(118372))