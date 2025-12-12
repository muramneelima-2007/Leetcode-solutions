class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        n=l//2 
        d={}
        for i in set(nums):
            c=nums.count(i)
            d[i]=c 
        for i, j in d.items():
            if(j>n):
                return i