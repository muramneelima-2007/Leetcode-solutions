class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs[0])
        c=0
        for i in range(n):
            l="A"
            for s in strs:
                if(s[i]>=l):
                    l=s[i]
                else:
                    c=c+1
                    break
        return c