class Solution:
    def minElement(self, nums: List[int]) -> int:
        li=[]
        m=10000
        for n in nums:
            s=0
            while(n!=0):
                t=n%10 
                s=s+t 
                n=n//10
            if(s<m):
                m=s

        return m