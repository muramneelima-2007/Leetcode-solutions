class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        s=[]
        val=0
        l=len(nums)
        for i in range(l):
            val=val+nums[i]
            s.append(val)
        las=s[l-1]
        for j in range(l):
            curr=abs((s[j]-nums[j])-(las-s[j]))
            res.append(curr)
        return res

