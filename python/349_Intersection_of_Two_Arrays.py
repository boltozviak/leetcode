class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        '''
        просто берём пересечение множеств
        '''
        return list(set(nums1) & set(nums2))