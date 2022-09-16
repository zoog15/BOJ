def third_jin(n):
    answer = ''

    while True:
        if n == 0:
            break
        answer += str(n%3)
        n //= 3

    return answer


def solution(n):
    answer = 0

    # 3진법 한 숫자 거꾸로 되서 나옴, third_num : str
    third_num = third_jin(n)

    for i in range(len(third_num)):
        if third_num[i] == '0':
            continue
        else:
            answer += int(third_num[i]) * pow(3,len(third_num)-1-i)

    return answer


print(solution(45))
print(solution(125))