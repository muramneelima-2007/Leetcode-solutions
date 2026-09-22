class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l=len(nums)
        c=0
        for i in range(l-1):
            for j in range(i,l):
                if(j<l-1):
                    if(nums[i]==nums[j+1]):
                        c=c+1 
        return c
        
