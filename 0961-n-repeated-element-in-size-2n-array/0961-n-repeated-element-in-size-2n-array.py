class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        l=len(nums)
        n=l//2 
        for i in nums:
            c=nums.count(i)
            if(c==n):
                res=i 
                break 
        return res