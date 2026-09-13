class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if(x<0):
        #     return False 
        # if(x==0):
        #     return True
        # n=""
        # s=str(x)
        # while(x!=0):
        #     t=x%10 
        #     n=n+str(t)
        #     x=x//10 
        # return s==n

        s=str(x)
        return s==s[::-1]