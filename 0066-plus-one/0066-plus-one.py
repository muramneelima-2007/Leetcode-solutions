class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="" 
        for i in digits:
            s=s+str(i)
        n=int(s)
        num=n+1 
        res=[]
        while(num!=0):
            t=num%10 
            res=[t]+res
            num=num//10 
        return res