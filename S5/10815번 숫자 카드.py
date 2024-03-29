def binary(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left+right)//2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return 0


n = int(input())

cards = list(map(int, input().split()))
cards.sort()

m = int(input())
nums = list(map(int, input().split()))

answer = []

for i in nums:
    answer.append(binary(cards, i))

print(*answer)