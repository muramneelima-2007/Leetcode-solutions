class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if(len(set(nums))<3):
            return max(nums)
        else:
            n=set(nums)
            li=list(n)
            li=sorted(li,reverse=True)
            return li[2]
