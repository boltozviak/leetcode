import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        '''
        1)создаём словарь частот элементов и список кортежей (частота,элемент)
        2)сортируем список по частоте
        3)ответ - последние k элементов из отсортированного списка
        '''
        freq_dict = Counter(nums)
        c = sorted([(f,v) for v,f in freq_dict.items()])
        return [num for freq, num in c[-k:]]
        
