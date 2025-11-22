class Solution:
    '''
    O(n)
    1)длина множества равна длине массива, если нет дубликатов => возвращаем False в таком случае
    '''
    def containsDuplicate(self, nums: list[int]) -> bool:
        return not(len(set(nums)) == len(nums))