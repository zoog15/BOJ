# 몇 개의 정수 받을건지
n = int(input())

# 입력받을 정수 들어갈 배열
nums = list(map(int, input().split()))

print(min(nums), end=' ')
print(max(nums))