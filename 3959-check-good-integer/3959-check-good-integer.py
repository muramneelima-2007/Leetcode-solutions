class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        sum1=0
        sum2=0
        while(n!=0):
            t=n%10 
            sum1+=t
            sum2+=(t*t)
            n=n//10 
        if(sum2-sum1>=50):
            return True 
        return False

