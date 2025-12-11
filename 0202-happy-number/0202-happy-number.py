class Solution:
    def isHappy(self, n: int) -> bool: 
        if(len(str(n))==1):
            if(n==1 or n==7):
                return True
            return False
        while(1):
            num=0
            while(n!=0):
                s=n%10
                num=num+s**2
                n=n//10 
            n=num
            if(len(str(n))==1):
                if(n==1 or n==7):
                    return True 
                return False
        