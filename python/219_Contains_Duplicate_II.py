class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        '''
        O(n)
        1)проходимся по массиву, если значения в словаре нет -> записываем 'значение - индекс'
        2)если значение есть -> проверяем условие: модуль разности предыдущего индекса(индекса в словаре) и нового индекса
        3)если выполняется -> True; если нет -> записываем новый индекс в словарь
        '''
        index_dict = {}
        for i in range(len(nums)):
            if nums[i] not in index_dict:
                index_dict[nums[i]] = i
            elif nums[i] in index_dict:
                if abs(i - index_dict[nums[i]]) <= k:
                    return True
                index_dict[nums[i]] = i
        return False