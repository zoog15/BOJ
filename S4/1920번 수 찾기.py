def binary_search(nums, target):
    # 이진 탐색으로 구현
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] > target:
                right = mid - 1
        else:
            left = mid + 1
    return 0


n = int(input())
nums = list(map(int, input().split()))

m = int(input())
mums = list(map(int, input().split()))

nums.sort()
for i in mums:
    target = i
    if binary_search(nums, target):
        print(1)
    else:
        print(0)

