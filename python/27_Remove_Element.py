class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        '''
        O(n)
        1)проходимся по массиву, и если элемент не равен val,
        записываем его в позицию pos и увеличиваем pos на 1 => pos - количество элементов не равных val
        '''
        pos = 0
        for n in range(len(nums)):
            if nums[n] != val:
                nums[pos] = nums[n]
                pos += 1
        return pos
            