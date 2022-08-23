n = int(input())

nums = [0,1,1]

for i in range(3, n+1):
    fibo = nums[i-2] + nums[i-1]
    nums.append(fibo)

print(nums[n])