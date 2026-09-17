class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            c=0 
            while(n!=0):
                n=n//10 
                c=c+1 
            if(c%2==0):
                res+=1 
        return res

        