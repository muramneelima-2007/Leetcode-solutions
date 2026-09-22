class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dict={}
        # for i in set(nums):
        #     dict[i]=0 
        # for i in nums:
        #     dict[i]=dict[i]+1 
        #     if(dict[i]>1):
        #         return True 
        # return False
        # (or)

        l1=len(nums)
        l2=len(set(nums))
        if(l1==l2):
            return False
        return True
        



        

