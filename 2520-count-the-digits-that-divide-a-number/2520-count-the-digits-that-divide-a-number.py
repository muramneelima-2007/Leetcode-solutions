class Solution:
    def countDigits(self, num: int) -> int:
        s=str(num)
        c=0
        l=len(s)
        temp=num
        if(num<=9):
            return 1 
        else:
            for i in range(l):
                n=temp%10
                if(num%n==0):
                    c=c+1
                temp=temp//10 
        return c

