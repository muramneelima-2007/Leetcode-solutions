class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        res=""
        n=len(s)
        for i in range(n):
            if(i+1<=k):
                res=s[i]+res
            else:
                res=res+s[i]
        return res