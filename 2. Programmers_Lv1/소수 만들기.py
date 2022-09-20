nums = [1,2,7,6,4]

def solution(nums):
    answer = 0

    for first in range(0, len(nums)-2):
        for second in range(first+1, len(nums)-1):
            for third in range(second+1, len(nums)):
                sum_num = nums[first] + nums[second] + nums[third]
                # 소수 판별하기
                for i in range(2, round(sum_num/2)):
                    if sum_num % i == 0:
                        break
                else:
                    answer += 1
    return answer


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))