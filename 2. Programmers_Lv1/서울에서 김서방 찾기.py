def solution(seoul):
    answer = ''

    x = seoul.index("Kim")

    answer = "김서방은 "+ str(x) + "에 있다"
    return answer


print(solution(["Jane","Kim"]))