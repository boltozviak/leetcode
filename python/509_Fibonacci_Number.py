class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1

        for i in range(2, n+1):
            tmp = a + b
            a = b
            b = tmp
        return b

    # def fib(self, n: int) -> int:
        # '''
        
        # '''
        # if n == 0:
        #     return 0

        # dp = [0] * (n + 1)
        # dp[1] = 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]
    
    # def fib(self, n: int) -> int:
    #     '''
    #     O(n) - через динамику
    #     '''
    #     cache = {}
    #     def inner(n):
    #         if n == 0:
    #             return 0
    #         if n == 1:
    #             return 1
            
    #         if n in cache:
    #             return cache[n]

    #         cache[n] =  inner(n - 1) + inner(n - 2)
    #         return cache[n]
        
    #     return inner(n)