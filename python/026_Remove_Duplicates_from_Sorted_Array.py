class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        '''
        O(n)
        
        '''
        k = 1
        prev_value = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev_value:
                nums[k] = nums[i]
                k += 1
                prev_value = nums[i]
        return k