def solution(phone_number):
    answer = ''
    length = len(phone_number)

    star = length - 4

    answer += '*'*star

    for i in range(star, length):
        answer += phone_number[i]

    return answer


print(solution("01033334444"))