class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        n=len(s)
        for i in range(n-1):
            n1=int(s[i])
            n2=int(s[i+1])
            if(abs(n1-n2)>2):
                return False 
        return True
