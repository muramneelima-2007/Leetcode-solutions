class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        s=0
        while n!=0:
            t=n%10
            p=p*t 
            s=s+t
            n=n//10 
        return p-s
