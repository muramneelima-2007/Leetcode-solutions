class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=len(nums)
        li=[]
        s=0
        for i in range(l):
            s=s+nums[i]
            li.append(s)
        return li
