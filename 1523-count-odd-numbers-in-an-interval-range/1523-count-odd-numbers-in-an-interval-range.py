class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def countOdDFrom1toN(n):
            if(n%2==1):
                return (n+1)//2 
            return n//2 
        n1=countOdDFrom1toN(low)
        n2=countOdDFrom1toN(high)
        count=0
        if(low%2==1):
            return n2-n1+1 
        return n2-n1
       