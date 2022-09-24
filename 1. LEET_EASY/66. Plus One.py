def solution(digits):
    num = ''
    answer = []

    for i in digits:
        num += str(i)

    i_num = str(int(num) + 1)

    for i in i_num:
        answer.append(i)

    return answer



print(solution([1,2,3]))
print(solution([4,3,2,1]))
print(solution([9]))