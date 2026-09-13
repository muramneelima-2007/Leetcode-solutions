class Solution:
    def fib(self, n: int) -> int:
        if(n<=1):
            return n
        p1=0
        p2=1
        cur=0
        for i in range(2,n+1):
            cur=p1+p2 
            p1=p2 
            p2=cur 
        return cur