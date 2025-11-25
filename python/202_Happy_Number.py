class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        1)создаём множество, в которое будем вкладывать уникальные числа
        2)если число 'счастливое' -> дойдёт до единицы
        3)если нет -> то в какой-то момент начнётся цикл повторяющихся значений => при первом повторе -> False
        '''
        s = set()
        while n != 0:
            n = sum([int(x) ** 2 for x in str(n)])
            if n not in s:
                s.add(n)
            else:
                return False
        return True
