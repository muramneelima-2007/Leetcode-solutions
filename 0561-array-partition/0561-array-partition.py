class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        n=len(nums)
        for i in range(0,n-1,2):
            a=min(nums[i],nums[i+1])
            total=total+a 
        return total