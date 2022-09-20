def solution(nums):
    half = len(nums)//2

    s_nums = set(nums)

    if half > len(s_nums):
        answer = len(s_nums)
    else:
        answer = half

    return answer


print(solution([3,1,2,3]))