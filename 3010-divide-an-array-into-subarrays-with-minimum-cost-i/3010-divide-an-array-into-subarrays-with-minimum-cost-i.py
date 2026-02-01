class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        summ=nums[0]
        n=nums[1:]
        n.sort()
        summ=summ+n[0]+n[1]
        return summ
        




        
        