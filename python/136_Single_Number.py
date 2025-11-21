class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        '''
        O(n) 
        1)проходимся по массиву
        2)если числа нет в множестве - добавляем его
        3)если число есть в множестве - удаляем его
        4)в множестве остаётся число без пары
        '''
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return s.pop()