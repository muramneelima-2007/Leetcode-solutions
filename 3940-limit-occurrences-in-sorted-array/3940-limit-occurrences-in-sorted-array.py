class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        n=len(nums)
        d={}
        res=[]
        for i in nums:
            d[i]=0
        for i in nums:
            d[i]=d[i]+1 
        for i,j in d.items():
            m=j
            if(j>k):
                m=k
            while(m!=0):
                res.append(i)
                m=m-1
        return res

        
