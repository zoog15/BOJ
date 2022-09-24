def solution(nums1, m, nums2, n):
    del nums1[m:]

    nums1 += nums2[:n]

    nums1.sort()


print(solution([1,2,3,0,0,0], 3, [2,5,6], 3))