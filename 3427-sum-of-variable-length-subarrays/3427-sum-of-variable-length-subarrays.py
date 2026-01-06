class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            start=max(0,(i-nums[i]))
            numbers=nums[start:i+1]
            res=res+sum(numbers)
        return res

