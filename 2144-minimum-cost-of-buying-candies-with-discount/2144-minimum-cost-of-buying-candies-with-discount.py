class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost=sorted(cost,reverse=True)
        n=len(cost)
        res=0
        for i in range(n):
            if((i+1)%3!=0):
                res=res+cost[i]
        return res



