class Solution:
    def numSteps(self, s: str) -> int:
        num=0
        l=len(s)
        for i in range(l):
            num=num+int(s[i])*(2**(l-i-1))
        c=0
        while(num!=1):
            if(num%2==0):
                num=num//2
                c=c+1
            else:
                num=num+1
                c=c+1
        return c

