class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        result = [0] * (m + n)
        first, second, third = 0, 0, 0
        while first < m and second < n:
            if nums1[first] < nums2[second]:
                result[third] = nums1[first]
                first += 1
            else:
                result[third] = nums2[second]
                second += 1
            third += 1
        while first < m:
            result[third] = nums1[first]
            first += 1
            third += 1
        while second < n:
            result[third] = nums2[second]
            second += 1
            third += 1
        for first in range(m + n):
            nums1[first] = result[first]