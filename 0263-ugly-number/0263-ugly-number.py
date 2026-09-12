class Solution:
    def isUgly(self, n: int) -> bool:
        if(n<=0):
            return False 
        if(n==1):
            return True
        li=[2,3,5]
        k=0
        while(k<3):
            while(n%li[k]==0):
                n=n//li[k] 
                if(n==1):
                    return True 
            k=k+1
        return False
           
        
            

        