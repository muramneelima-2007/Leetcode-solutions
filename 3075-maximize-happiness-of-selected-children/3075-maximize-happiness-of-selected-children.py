class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        if(set(happiness)=={1}):
            return 1
        happiness.sort()
        total=0
        c=1
        while(k!=0):
            val=happiness[-1]
            total=total+val 
            if(len(happiness)==1):
                return total
            happiness.pop()
            happiness[-1]=happiness[-1]-c
            k=k-1
            c=c+1
        return total

