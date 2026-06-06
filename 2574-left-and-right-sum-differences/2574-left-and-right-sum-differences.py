class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # res=[]
        # s=[]
        # val=0
        # l=len(nums)
        # for i in range(l):
        #     val=val+nums[i]
        #     s.append(val)
        # las=s[l-1]
        # for j in range(l):
        #     curr=abs((s[j]-nums[j])-(las-s[j]))
        #     res.append(curr)
        # return res
        n=len(nums)
        la=[]
        ra=[]
        sum1=0
        summ=sum(nums)
        la=[sum1]
        for i in range(n):
            sum1+=nums[i]
            la.append(sum1)
            ra.append(summ-sum1)
        res=[]
        for i in range(n):
            res.append(abs(la[i]-ra[i]))
        return res