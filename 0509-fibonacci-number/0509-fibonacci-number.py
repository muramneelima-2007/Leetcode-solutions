class Solution:
    def fib(self, n: int) -> int:
        def fibanacci(n):
            if(n==0):
                return 0
            elif(n==1):
                return 1
            else:
                return fibanacci(n-1)+fibanacci(n-2)
        return fibanacci(n)