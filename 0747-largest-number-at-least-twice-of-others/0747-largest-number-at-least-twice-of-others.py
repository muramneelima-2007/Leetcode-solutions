class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=max(nums)
        for i in nums:
            if(i==maxi):
                continue
            elif(i*2<=maxi):
                continue 
            else:
                return -1 
        for i in range(n):
            if(nums[i]==maxi):
                return i
