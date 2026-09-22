class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=len(nums)
        li=[]
        for i in range(l):
            c=0
            for j in range(l):
                if(nums[i]>nums[j]):
                    c=c+1 
            li=li+[c]
        return li
