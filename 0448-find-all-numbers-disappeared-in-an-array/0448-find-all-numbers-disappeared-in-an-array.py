class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[False]*n
        nums.sort()
        for i in range(n):
            arr[nums[i]-1]=True
        res=[]
        for i in range(len(arr)):
            if(arr[i]==False):
                res.append(i+1)
        return res

            
        

        


          