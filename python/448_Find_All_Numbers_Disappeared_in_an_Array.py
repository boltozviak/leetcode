class Solution:
    # def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    #     '''
    #     O(n)
    #     '''
    #     n = len(nums)
    #     res = []
    #     for i in range(n):
    #         v = abs(nums[i]) - 1
    #         if nums[v] > 0:
    #             nums[v] = nums[v] * (-1)
    #     for i in range(n):
    #         if nums[i] > 0:
    #             res.append(i + 1)
    #     return res
    
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        '''
        O(n)
        '''
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]