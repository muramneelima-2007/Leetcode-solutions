class Solution:
    def addDigits(self, num: int) -> int:
        sum=num
        while(len(str(sum))!=1):
            s=0
            while(sum!=0):
                t=sum%10 
                s=s+t
                sum=sum//10  
            sum=s 
        return sum

         


