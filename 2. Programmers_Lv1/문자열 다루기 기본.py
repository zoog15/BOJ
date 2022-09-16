def solution(s):
    answer = True

    if len(s) != 4 and len(s) != 6:
        return False
    else:
        for i in s:
            if not "0" <= i <= "9":
                return False

    return answer


print(solution("a234"))
print(solution("1234"))