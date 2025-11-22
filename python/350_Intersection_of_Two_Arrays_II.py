from collections import defaultdict

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq_dict1 = defaultdict(int)
        for num in nums1:
            freq_dict1[num] += 1
        freq_dict2 = defaultdict(int)
        for num in nums2:
            freq_dict2[num] += 1
        intersec = list(set(nums1) & set(nums2))
        res = []
        for i in intersec:
            res += [i] * min(freq_dict1[i], freq_dict2[i])
        return res
