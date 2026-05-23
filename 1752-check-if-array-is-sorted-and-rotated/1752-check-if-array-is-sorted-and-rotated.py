class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        sortedArr=sorted(nums)
        while(n!=0):
            nums=[nums[-1]]+nums[:-1]
            if(nums==sortedArr):
                return True 
            n=n-1
        return False

