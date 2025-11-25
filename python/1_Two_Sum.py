class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        O(n)
        1)проходимся по массиву, и вычисляем для каждого элемента разность с target
        2)если такая разность уже есть в словаре - возвращаем ответ
        3)если нет - добавляем текущий элемент в словарь
        '''
        num_dict = {}
        for i, v in enumerate(nums):
            zaz = target - v
            if zaz in num_dict:
                return [num_dict[zaz], i]
            num_dict[v] = i
            
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     ''' 
    #     O(n log n) - из-за .sort()
    #     Два указателя:
    #     1)создаём список кортежей (value,index)
    #     2)сортируем этот список по значению(value)
    #     3)двумя указателями ищем подходящие значения
    #     4)когда нашли - возвращаем список из индексов, соответствующих значениям
    #     '''
    #     index_arr = [(value, index) for index, value in enumerate(nums)]
    #     index_arr.sort()
    #     left = 0
    #     right = len(nums) - 1
    #     while left < right:
    #         value = index_arr[left][0] + index_arr[right][0]
    #         if value == target:
    #             return [index_arr[left][1], index_arr[right][1]]
    #         elif value < target:
    #             left += 1
    #         elif value > target:
    #             right -= 1
