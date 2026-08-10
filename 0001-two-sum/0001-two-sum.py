class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        li=[]
        for i in range(l-1):
            for j in range(i+1,l):
                if(nums[i]+nums[j]==target):
                    li=[i,j]
                    break
            
        return li
