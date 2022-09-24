def solution(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        for i in nums:
            if i > target:
                index = nums.index(i)
                break
            else:
                index = len(nums)
        return index


print(solution([1,3,5,6],5))
print(solution([1,3,5,6],2))
print(solution([1,3,5,6],7))


