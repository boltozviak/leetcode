class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        '''
        O(n)
        1)вычисляем сумму всех натуральных до n включительно по формуле 'n * (n + 1) / 2'
        2)вычитаем из этой суммы сумму элементов массива => находим пропущенное число
        '''
        n = len(nums)
        return int((n * (n + 1) / 2 - sum(nums)))