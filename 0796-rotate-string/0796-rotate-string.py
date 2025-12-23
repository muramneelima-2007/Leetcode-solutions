class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        k=0
        s1=""
        while(n!=k):
            if(s==goal):
                return True 
            else:
                s1=s[1:]+s[0]
                s=s1
            k=k+1 
        return False