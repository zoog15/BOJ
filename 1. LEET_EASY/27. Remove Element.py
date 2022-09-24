def removeElement(nums, val):
    while nums.count(val):
        nums.remove(val)

    return len(nums)


print(removeElement([3,2,2,3],3 ))


