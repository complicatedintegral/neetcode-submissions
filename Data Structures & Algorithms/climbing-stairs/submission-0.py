class Solution:
    def climbStairs(self, n: int) -> int:
        
        '''
        def fib(x): # naive recursion, very high complexity
            if x <= 0:
                return 0
            elif x == 1:
                return 1
            else:
                return fib(x-1) + fib(x-2)
        '''

        def fib(x): # efficient fibronacci function
            i = 1
            j = 1
            for _ in range(x-1):
                i, j = j, i+j
            return j

        return fib(n)