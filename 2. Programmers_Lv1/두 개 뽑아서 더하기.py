def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            nums = numbers[i] + numbers[j]
            if nums not in answer:
                answer.append(nums)

    answer.sort()

    return answer


print(solution([2,1,3,4,1]))