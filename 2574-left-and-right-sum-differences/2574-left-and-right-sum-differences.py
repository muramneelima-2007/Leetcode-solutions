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
        
        # n = len(nums)
        # left = [0] * n
        # right = [0] * n
        # fini = [0] * n

        # sum1 = 0
        # sum2 = 0

        # for i in range(n):
        #     sum1 += nums[i]
        #     sum2 += nums[n - i - 1]
        #     left[i] = sum1
        #     right[n - i - 1] = sum2

        # for i in range(n):
        #     fini[i] = abs(left[i] - right[i])

        # return fini