def twoSum(nums, target):
    ans = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                ans.append(i)
                ans.append(j)
                break

    return ans


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))