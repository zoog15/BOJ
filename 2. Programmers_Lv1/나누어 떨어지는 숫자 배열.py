def solution(arr, divisor):
    answer = []
    arr.sort()

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if answer:
        return answer
    else:
        return [-1]


print(solution([5,9,7,10],5))