class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Сортировка Шелла
        """
        increment = 4
        while increment > 0:
            for i in range(len(nums)):
                j = i
                temp = nums[i]
                while j >= increment and nums[j - increment] > temp:
                    nums[j] = nums[j - increment]
                    j = j - increment
                nums[j] = temp
            if increment > 1:
                increment //= 2
            else:
                break