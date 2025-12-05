class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for i in range(1,n):
            left=nums[:i]
            right=nums[i:]
            leftSum=sum(left)
            rightSum=sum(right)
            diff=leftSum-rightSum
            if(diff%2==0):
                count+=1 
        return count