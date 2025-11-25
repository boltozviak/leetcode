class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        '''
        O(n ** 2)
        1)создаём numRows членов в res
        2)для каждого члена создаём ans, который будет добавлен
        3)ans сначала заполняем единицами, а члены с индексами [1,i-1],
        заменяем на сумму элементов из предыдущего члена res с таким же индексом и (индексом - 1)
        '''
        res = []
        for i in range(numRows):
            ans = [1] * (i + 1)
            for j in range(1, i):
                ans[j] = (res[-1][j - 1] + res[-1][j])
            res.append(ans)
            i += 1
        return res


    # def generate(self, numRows: int) -> list[list[int]]:
    #     '''
    #     первое, искусственое решение, т.к. вводятся начальные условия i и res
    #     '''
    #     if numRows == 1:
    #         return [[1]]
    #     elif numRows == 2:
    #         return [[1], [1,1]]
    #     else:
    #         i = 2
    #         res = [[1], [1,1]]
    #         while i != numRows:
    #             ans = [1]
    #             for j in range(1, i):
    #                 ans.append(res[i - 1][j - 1] + res[i - 1][j])
    #             ans.append(1)
    #             res.append(ans)
    #             i += 1
    #         return res