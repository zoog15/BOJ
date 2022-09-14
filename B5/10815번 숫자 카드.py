def binary_search(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            return 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0


n = int(input())
nums = list(map(int, input().split()))
m = int(input())
mums = list(map(int, input().split()))

nums.sort()
ans = []
for i in mums:
    ans.append(binary_search(nums, i))

for i in ans:
    print(i, end=' ')