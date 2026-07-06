class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        rc=0 
        lc=0
        for i in s:
            if(i=='R'):
                rc+=1 
            else:
                lc+=1 
            if(rc==lc):
                count+=1 
                rc=0 
                lc=0 
        return count