class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum=[]
        for i in accounts:
            s=0
            for j in i:
                s+=j 
            sum=sum+[s]
        return max(sum)

            
        