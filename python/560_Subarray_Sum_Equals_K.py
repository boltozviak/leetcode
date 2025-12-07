class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        cnt = 0
        sum_dict = {}
        z = 0
        for i in range(len(nums)):
            z += nums[i]
            if z == k:
                cnt += 1
            
            if (z - k) in sum_dict :
                cnt += sum_dict[z - k]

            if z in sum_dict:
                sum_dict[z] += 1
            else:
                sum_dict[z] = 1
        return cnt