from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        '''
        1)создаём словарь частот элементов и список кортежей (частота,элемент)
        2)сортируем список по частоте(значению)
        3)ответ - последние k элементов из отсортированного списка
        '''
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        c = sorted([(f,v) for v,f in freq_dict.items()])
        return [num for freq, num in c[-k:]]
        
