def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ':
            answer += ' '
        else:
            lowup = ord(i)
            cizer = lowup + n
            if 97 <= lowup <= 122 and cizer > 122:
                cizer -= 26
            elif 65 <= lowup <= 90 and 90 < cizer:
                cizer -= 26
            answer += chr(cizer)

    return answer


print(solution("AB",1))
print(solution("ABCDEFZ", 5))
print(solution("a B z",4))
print(solution("AaZz", 25))