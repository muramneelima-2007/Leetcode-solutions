class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        # n=len(batteryPercentages)
        # c=0
        # k=0
        # s=[]
        # while k!=n:
        #     if(batteryPercentages[k]>0):
        #         c=c+1
        #         for i in range(k+1,n):
        #             s.append(batteryPercentages[i]-1)
        #         batteryPercentages=batteryPercentages[:k+1]+s
        #         s=[]
        #     k=k+1
        # return c
        n=len(batteryPercentages)
        c=0
        k=0
        s=[]
        while k!=n:
            batteryPercentages[k]=batteryPercentages[k]-c
            batteryPercentages[k]=max(batteryPercentages[k],0)
            if(batteryPercentages[k]>0):
                c=c+1
            k=k+1 
        return c